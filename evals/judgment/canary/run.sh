#!/bin/sh
# Judge canary: two bad reports through the real runner + real Sonnet judge.
# Expect judgment well below the pilot (<= 0.34) and valid = 0 for both.
set -e
cd "$(dirname "$0")/../../.."
D=.claude/hillclimb/forecast-judgment-canary
for k in idk wrongq; do
  mkdir -p "$D-$k"; cp .claude/hillclimb/forecast-judgment/_state.json "$D-$k/_state.json"
  PATH="$PWD/evals/judgment/canary/bin:$PATH" CANARY=$k node evals/judgment/run_eval.mjs --flow "$D-$k" --variant baseline --model claude-opus-5-5 --cases replay-2026-11-08 --approve-harness 2>&1 | tail -1
  python3 -c "import json,sys;r=json.loads(open(sys.argv[1]).readline());print(sys.argv[2],r['grade']);print(r['explanation']['judgment'])" "$D-$k/baseline/results.jsonl" $k
done
