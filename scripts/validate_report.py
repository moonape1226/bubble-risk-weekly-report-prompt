#!/usr/bin/env python3
"""Deterministic pre-archive validation gate for the bubble-risk weekly report.

Checks the locked skeleton (12 sections, exact headings, §1/§2/§3 columns),
the exact final disclaimer line, the score-JSON schema / arithmetic / tier,
bar-chart-vs-score consistency, the 總評 line, and that no ASCII '~' (a '~' pair
renders as strikethrough on the blob view, and a '\\~' escape prints a literal
backslash on the Python-Markdown Pages build) leaks into report-visible text.
stdlib only.

Usage: python3 validate_report.py <report.md> [--coverage-rows N]
Exits 0 when every check passes; prints one FAIL line per defect and exits 1.
"""
import json, re, sys
from datetime import datetime

TITLE_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2}) 市場泡沫風險評估報告$")
HEADINGS = [
    "## §1 六維度風險條圖",
    "## §2 歷史錨點相似度",
    "## §3 三角訊號",
    "## 六維度評分",
    "## 綜合分數",
    "## 歷史泡沫週期對比",
    "## 機構情緒對照",
    "## 本次新增訊號",
    "## 數據附錄",
    "## 本次分數存檔",
]
S1_HEADER = "| 維度 | 條圖 | 本次 | 前次 | Δ |"
S2_HEADER = "| 錨點 | 相似度 | 條圖 | 標記 |"
S3_HEADER = "| 指標 | 本次數值 | vs 前次 |"
ANCHORS = ["1997 早期建設", "1998 LTCM 衝擊", "1999 晚期狂熱",
           "2000/3 頂點", "2021/12 Meme 頂"]
S3_INDICATORS = ("S&P 500", "WTI", "10Y")
FINAL_LINE = "本報告為相對風險溫度計，非擇時訊號。"
DIMS = [("估值溢價", "valuation"), ("市場廣度", "breadth"), ("投機行為", "speculation"),
        ("散戶情緒", "retail"), ("貨幣與信貸環境", "monetary"), ("結構性槓桿", "structural")]
WEIGHTS = {"valuation": 22, "breadth": 13, "speculation": 18,
           "retail": 12, "monetary": 20, "structural": 15}
TIERS = [(0, 19, "低"), (20, 39, "溫和"), (40, 64, "警戒"), (65, 84, "高"), (85, 100, "極度狂熱")]
REGIMES = {"穩定共存", "同向偏高", "分歧", "基準日", "不可判"}
JSON_KEYS = {"date", "iso_week", "weekday", "timezone", "valuation", "breadth", "speculation",
             "retail", "monetary", "structural", "total", "tier", "regime"}
STATUS_TOKENS = ("✓ API", "✓ DIRECT", "✓ SEARCH-VERIFIED", "derived",
                 "✗ NOT DISCLOSED", "⛔ FETCH FAILED")
BOX_CHARS = "╔╗╚╝║═╠╣╬┌┐└┘─│├┤┬┴┼"

fails = []


def fail(msg):
    fails.append(msg)


def cell_int(cell):
    """Int out of a table cell, tolerating **bold**, ⚠/◆/【tier】 marks, U+2212 minus."""
    t = cell.replace("*", "").replace("⚠", "").replace("◆", "").replace("−", "-")
    m = re.search(r"-?\d+", t)
    return int(m.group()) if m else None


def table_rows(lines, header):
    """Data rows of the markdown table whose header row is exactly `header`."""
    try:
        i = lines.index(header)
    except ValueError:
        return None
    rows = []
    for line in lines[i + 1:]:
        if not line.startswith("|"):
            break
        if re.match(r"^\|[\s:|-]+\|$", line):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def prompt_bullet_count(path):
    """Top-level `- ` bullets under `# Data sources` in the prompt file
    (fenced code blocks and indented sub-bullets excluded)."""
    n, in_sources, fenced = 0, False, False
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith("# "):
            in_sources = line.startswith("# Data sources")
            continue
        if in_sources and line.startswith("- "):
            n += 1
    return n


def check_bar(bar, score, where):
    filled, empty = bar.count("▰"), bar.count("▱")
    if filled + empty != 10:
        fail(f"{where}: 條圖非固定 10 格（{filled}▰+{empty}▱）")
    elif score is not None and filled != score // 10:
        fail(f"{where}: 條圖 {filled} 格 ≠ floor({score}/10)")


def main():
    path = sys.argv[1]
    cov_expected = None
    if "--coverage-rows" in sys.argv:
        cov_expected = int(sys.argv[sys.argv.index("--coverage-rows") + 1])
    elif "--prompt" in sys.argv:
        cov_expected = prompt_bullet_count(sys.argv[sys.argv.index("--prompt") + 1])
    text = open(path, encoding="utf-8").read()
    lines = [l.rstrip() for l in text.splitlines()]
    body = [l for l in lines if l.strip()]
    if body and body[0].startswith("> [DRY RUN]"):
        body = body[1:]

    # title / meta / 總評
    report_date = None
    m = TITLE_RE.match(body[0]) if body else None
    if not m:
        fail("首行不是 `# <YYYY-MM-DD> 市場泡沫風險評估報告`")
    else:
        report_date = m.group(1)
    if len(body) > 1 and not body[1].startswith("> 報告日期："):
        fail("第二行不是 `> 報告日期：...` meta 行")
    zy = re.search(r"^\*\*總評\*\*：總分 (\d+)【(低|溫和|警戒|高|極度狂熱)】（Δ ([^）]*)）；"
                   r"扳機狀態：(未擊發|初啟|已擊發)；最貼近錨點：(.+?)（(\d+)%）。$",
                   text, re.M)
    if not zy:
        fail("缺 `**總評**：總分 <X>【<tier>】（Δ ...）；扳機狀態：...；最貼近錨點：...（XX%）。` 行")

    # headings: exact set, order, no extras
    h2 = [l for l in lines if l.startswith("## ")]
    if h2 != HEADINGS:
        fail(f"`## ` 標題與 12-section 鎖不符：{h2}")
    h1 = [l for l in body if l.startswith("# ")]
    if len(h1) != 1:
        fail(f"`# ` 標題應恰一個，實得 {len(h1)}")

    # final line
    if body and body[-1] != FINAL_LINE:
        fail(f"最後一行不是「{FINAL_LINE}」，實得「{body[-1]}」")

    # forbidden characters / terms
    hit = sorted({c for c in text if c in BOX_CHARS})
    if hit:
        fail(f"含禁用框線字元：{''.join(hit)}")
    # ASCII '~' is unsafe in report-visible text under BOTH renderers this
    # archive uses, so neither a bare '~' nor a '\~' escape is allowed:
    #  - GitHub blob view (GFM) parses a '~' pair on one line/paragraph as a
    #    strikethrough delimiter, striking the span between them and corrupting
    #    any adjacent **bold**;
    #  - GitHub Pages (scripts/build_site.py, Python-Markdown) does not treat
    #    '\~' as an escape and prints a literal backslash.
    # Use ≈ / 約 instead. Ignore fenced/inline code and URLs.
    tilde_lines, in_fence = [], False
    for n, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = re.sub(r"`[^`]*`", "", l)
        stripped = re.sub(r"https?://\S+", "", stripped)
        if "~" in stripped:
            tilde_lines.append(n)
    if tilde_lines:
        shown = ", ".join(map(str, tilde_lines[:10]))
        more = "" if len(tilde_lines) <= 10 else f" 等共 {len(tilde_lines)} 行"
        fail(f"含 ASCII `~`（blob GFM 成對→刪除線並破壞 **粗體**；Pages 的 "
             f"Python-Markdown 不吃 \\~ 轉義、會印出反斜線）；報告可見文字改用 "
             f"≈／約。行：{shown}{more}")
    # 本期 is banned in section names, table columns, meta/labels, 本次新增訊號,
    # and 本次分數存檔 — not in ordinary prose
    section = None
    for l in lines:
        if l.startswith("## "):
            section = l
        if "本期" in l and (l.startswith(("#", "|", ">", "**"))
                            or section in ("## 本次新增訊號", "## 本次分數存檔")):
            fail(f"「本期」出現在鎖定位置（terminology lock）：{l.strip()[:60]}")

    # §1 table
    s1 = table_rows(lines, S1_HEADER)
    s1_scores, s1_total, s1_total_delta = {}, None, None
    if s1 is None:
        fail(f"缺 §1 表頭 `{S1_HEADER}`")
    else:
        names = [r[0].replace("*", "") for r in s1 if r]
        expect = [d[0] for d in DIMS] + ["加權總分"]
        if names != expect:
            fail(f"§1 列名/順序錯誤：{names}")
        for r in s1:
            if len(r) != 5:
                fail(f"§1 欄數 ≠ 5：{r}")
                continue
            name = r[0].replace("*", "")
            score = cell_int(r[2])
            check_bar(r[1], score, f"§1 {name}")
            prev, delta = cell_int(r[3]), cell_int(r[4])
            if score is not None and prev is not None and delta is not None and score - prev != delta:
                fail(f"§1 {name}: Δ={delta} ≠ 本次{score}−前次{prev}")
            if name == "加權總分":
                s1_total, s1_total_delta = score, delta
            else:
                s1_scores[name] = score

    # §2 table
    s2 = table_rows(lines, S2_HEADER)
    closest = None
    if s2 is None:
        fail(f"缺 §2 表頭 `{S2_HEADER}`")
    else:
        names = [r[0].replace("*", "") for r in s2 if r]
        if names != ANCHORS:
            fail(f"§2 錨點列應為固定五錨點（依序 {ANCHORS}），實得：{names}")
        marked = [r for r in s2 if len(r) == 4 and r[3] == "◀ 最貼近"]
        if len(marked) != 1:
            fail(f"§2「◀ 最貼近」應恰一列，實得 {len(marked)}")
        pcts = []
        for r in s2:
            if len(r) != 4:
                fail(f"§2 欄數 ≠ 4：{r}")
                pcts.append(None)
                continue
            # full-format checks: cell_int-style loose parsing accepted
            # "40.5%" / "foo50%", and substring matching accepted decorated
            # marker cells — a silent None would also switch off the
            # marked-is-max check below
            m2 = re.fullmatch(r"(\d{1,3})%", r[1])
            pct = int(m2.group(1)) if m2 else None
            pcts.append(pct)
            check_bar(r[2], pct, f"§2 {r[0]}")
            if pct is None:
                fail(f"§2 {r[0]}: 相似度欄格式應為 `<整數>%`：{r[1]!r}")
            elif pct % 5 != 0:
                fail(f"§2 {r[0]}: 相似度 {pct}% 非 5% 刻度")
            elif pct > 100:
                fail(f"§2 {r[0]}: 相似度 {pct}% 超出 0-100")
            if r[3] not in ("", "◀ 最貼近"):
                fail(f"§2 {r[0]}: 標記欄僅允許空白或「◀ 最貼近」：{r[3]!r}")
        if len(marked) == 1:
            closest = (marked[0][0], pcts[s2.index(marked[0])])
        if len(marked) == 1 and pcts and all(p is not None for p in pcts):
            best_idx = max(range(len(pcts)), key=lambda i: pcts[i])  # first of ties
            mark_idx = s2.index(marked[0])
            if mark_idx != best_idx:
                fail(f"§2「◀ 最貼近」應標最高相似度列（同分取表列較前者）："
                     f"標記 {s2[mark_idx][0]}（{pcts[mark_idx]}%），"
                     f"應為 {s2[best_idx][0]}（{pcts[best_idx]}%）")

    if lines.count(S3_HEADER) != 1:
        fail(f"§3 表頭 `{S3_HEADER}` 應恰出現一次")
    else:
        s3 = table_rows(lines, S3_HEADER)
        if len(s3) != 3:
            fail(f"§3 應恰 3 列（S&P 500 / WTI / 10Y），實得 {len(s3)} 列")
        else:
            for r, key in zip(s3, S3_INDICATORS):
                if len(r) != 3:
                    fail(f"§3 欄數 ≠ 3：{r}")
                elif key not in r[0]:
                    fail(f"§3 列名應含「{key}」：{r[0]}")

    # §3 結論行：扳機狀態三態，供總評 cross-check
    s3_trigger = None
    if "## §3 三角訊號" in lines and "## 六維度評分" in lines:
        seg = lines[lines.index("## §3 三角訊號"):lines.index("## 六維度評分")]
        concl = next((l for l in seg if l.replace("*", "").startswith("結論：")), None)
        if concl is None:
            fail("§3 缺 `**結論**：` 行")
        else:
            m3 = re.search(r"扳機狀態：(未擊發|初啟|已擊發)", concl.replace("*", ""))
            if not m3:
                fail(f"§3 結論行缺「扳機狀態：<未擊發/初啟/已擊發>」：{concl[:60]}")
            else:
                s3_trigger = m3.group(1)

    # 總評 cross-checks（Δ 對 §1 加權總分列、扳機狀態對 §3 結論）
    if zy:
        if s3_trigger and zy.group(4) != s3_trigger:
            fail(f"總評扳機狀態 {zy.group(4)} ≠ §3 結論 {s3_trigger}")
        zy_delta = cell_int(zy.group(3))
        if (zy_delta is None) != (s1_total_delta is None) or (
                zy_delta is not None and zy_delta != s1_total_delta):
            fail(f"總評 Δ「{zy.group(3)}」 ≠ §1 加權總分列 Δ {s1_total_delta}")

    # score JSON
    jm = re.findall(r"```json\s*\n(.*?)```", text, re.S)
    score = None
    if not jm:
        fail("缺 ```json 分數存檔區塊")
    else:
        try:
            score = json.loads(jm[-1])
        except ValueError as e:
            fail(f"score JSON 無法解析：{e}")
        else:
            if not isinstance(score, dict):
                fail(f"score JSON 應為 JSON 物件（dict），實得：{jm[-1].strip()[:40]!r}")
                score = None
    if score is not None:
        if set(score) != JSON_KEYS:
            fail(f"score.json 鍵不符 schema：多 {set(score)-JSON_KEYS}、缺 {JSON_KEYS-set(score)}")
        else:
            # type/range gate first: bool is an int subclass and str * int
            # concatenates, so the arithmetic below runs only on true ints
            nums_ok = True
            for _, key in DIMS:
                v = score[key]
                if type(v) is not int or not 0 <= v <= 100:
                    fail(f"score.json {key}={v!r} 非 0-100 整數")
                    nums_ok = False
            if type(score["total"]) is not int or not 0 <= score["total"] <= 100:
                fail(f"score.json total={score['total']!r} 非 0-100 整數")
                nums_ok = False
            if nums_ok:
                x100 = sum(score[k] * w for k, w in WEIGHTS.items())
                want_total = (x100 + 50) // 100  # half-up
                if score["total"] != want_total:
                    fail(f"total={score['total']} ≠ 加權 half-up {want_total}（{x100/100}）")
                tier = next(t for lo, hi, t in TIERS if lo <= score["total"] <= hi)
                if score["tier"] != tier:
                    fail(f"tier={score['tier']} ≠ 對照表 {tier}（total {score['total']}）")
            # string fields gated the same way: [] is unhashable against the
            # REGIMES set and strptime(None) raises TypeError, not ValueError
            strs_ok = True
            for key in ("date", "iso_week", "weekday", "timezone", "tier", "regime"):
                if type(score[key]) is not str:
                    fail(f"score.json {key}={score[key]!r} 非字串")
                    strs_ok = False
            if strs_ok:
                if score["regime"] not in REGIMES:
                    fail(f"regime={score['regime']!r} 不在允許值 {sorted(REGIMES)}")
                if score["timezone"] != "Asia/Taipei":
                    fail(f"timezone={score['timezone']!r} ≠ Asia/Taipei")
                if report_date and score["date"] != report_date:
                    fail(f"score.json date={score['date']} ≠ 標題日期 {report_date}")
                try:
                    d = datetime.strptime(score["date"], "%Y-%m-%d")
                    if score["weekday"] != d.strftime("%A"):
                        fail(f"weekday={score['weekday']} ≠ {d.strftime('%A')}")
                    if score["iso_week"] != d.strftime("%G-W%V"):
                        fail(f"iso_week={score['iso_week']} ≠ {d.strftime('%G-W%V')}")
                except ValueError:
                    fail(f"date={score['date']!r} 非 YYYY-MM-DD")
            # cross-checks vs §1 and 總評
            for zh, key in DIMS:
                if zh in s1_scores and s1_scores[zh] != score[key]:
                    fail(f"§1 {zh}={s1_scores[zh]} ≠ score.json {key}={score[key]}")
            if s1_total is not None and s1_total != score["total"]:
                fail(f"§1 加權總分 {s1_total} ≠ score.json total {score['total']}")
            if zy:
                if int(zy.group(1)) != score["total"] or zy.group(2) != score["tier"]:
                    fail(f"總評 {zy.group(1)}【{zy.group(2)}】 ≠ score.json "
                         f"{score['total']}【{score['tier']}】")
                if closest and (zy.group(5) != closest[0] or int(zy.group(6)) != closest[1]):
                    fail(f"總評錨點 {zy.group(5)}（{zy.group(6)}%） ≠ §2 ◀ 列 "
                         f"{closest[0]}（{closest[1]}%）")

    # Coverage table
    cov_header = next((l for l in lines if l.startswith("|") and "維度 / source bullet" in l), None)
    if cov_header is None:
        fail("缺 Coverage 表（表頭含 `維度 / source bullet`）")
    else:
        rows = table_rows(lines, cov_header)
        for r in rows:
            if not any(tok in r[-1] for tok in STATUS_TOKENS):
                fail(f"Coverage 列缺最終狀態：{r[0]}")
        firsts = [r[0] for r in rows]
        dup = sorted({x for x in firsts if firsts.count(x) > 1})
        if dup:
            fail(f"Coverage 首欄重複（每個 source bullet 恰一列）：{dup[:5]}")
        if cov_expected is not None and len(rows) != cov_expected:
            fail(f"Coverage 列數 {len(rows)} ≠ 預期 {cov_expected}")

    if fails:
        for f in fails:
            print(f"FAIL: {f}")
        print(f"\n{len(fails)} failure(s).")
        sys.exit(1)
    print("PASS: all report-structure checks passed.")


if __name__ == "__main__":
    main()
