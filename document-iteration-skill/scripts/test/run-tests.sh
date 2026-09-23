#!/bin/bash
#
# Test runner for cleanup.py
# Runs each *-input.md fixture through the script and diffs against *-result.md
#

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CLEANUP="$(dirname "$SCRIPT_DIR")/cleanup.py"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

passed=0
failed=0

for input_file in "$SCRIPT_DIR"/*-input.md; do
    test_name=$(basename "$input_file" -input.md)
    result_file="${input_file/-input.md/-result.md}"

    tmp_file=$(mktemp)
    cp "$input_file" "$tmp_file"
    python3 "$CLEANUP" "$tmp_file" > /dev/null 2>&1

    if diff -u "$result_file" "$tmp_file" > /dev/null; then
        echo -e "${GREEN}PASS${NC}: $test_name"
        passed=$((passed + 1))
    else
        echo -e "${RED}FAIL${NC}: $test_name"
        diff -u "$result_file" "$tmp_file" | sed 's/^/    /'
        failed=$((failed + 1))
    fi

    rm "$tmp_file"
done

echo ""
echo "$passed passed, $failed failed"
[[ $failed -eq 0 ]]
