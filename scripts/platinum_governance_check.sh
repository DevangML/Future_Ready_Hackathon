#!/usr/bin/env bash
# ==============================================================================
# BMad AI OS - Platinum Governance Gate Check
# Validates: Constitution, Agent Manifest, Sentrux rules, Semgrep, Cursor rules
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== [BMad AI OS] Platinum Governance Gate Check ==="
FAILS=0

check_file() {
  local file="$1"
  local desc="$2"
  if [ -f "$file" ]; then
    echo "  [PASS] $desc found: $file"
  else
    echo "  [FAIL] Missing $desc: $file"
    FAILS=$((FAILS + 1))
  fi
}

check_content() {
  local file="$1"
  local pattern="$2"
  local desc="$3"
  if grep -qi "$pattern" "$file" 2>/dev/null; then
    echo "  [PASS] Verified $desc in $file"
  else
    echo "  [FAIL] Missing $desc in $file"
    FAILS=$((FAILS + 1))
  fi
}

echo "--> 1. Validating Constitution..."
CONST_FILE=".specify/memory/constitution.md"
check_file "$CONST_FILE" "Supreme Constitution"
if [ -f "$CONST_FILE" ]; then
  check_content "$CONST_FILE" "Article I" "Article I"
  check_content "$CONST_FILE" "Article VII" "Article VII"
  check_content "$CONST_FILE" "Article VI-A" "Article VI-A (Sentrux sequence)"
  check_content "$CONST_FILE" "Article VI-B" "Article VI-B (Token Economy)"
  check_content "$CONST_FILE" "Article VI-C" "Article VI-C (Add-ons)"
  check_content "$CONST_FILE" "Strict LOC Gate" "User Rule: 200 LOC Gate"
  check_content "$CONST_FILE" "Strict TDD" "User Rule: TDD bmad-tea"
fi

echo "--> 2. Validating Agent Manifest..."
check_file "AGENTS.md" "Agent Manifest"
if [ -f "AGENTS.md" ]; then
  check_content "AGENTS.md" "Governance & Gate Agent" "Governance Role"
  check_content "AGENTS.md" "Graph-First Retrieval" "Token Economy Policy"
fi

echo "--> 3. Validating Sentrux Boundaries..."
check_file ".sentrux/rules.toml" "Sentrux Rules"

echo "--> 4. Validating Semgrep Rule Packs..."
check_file ".semgrep/platform-baseline.yml" "Platform Baseline Rule Pack"
check_file ".semgrep/python-safety.yml" "Python Safety Rule Pack"
check_file ".semgrep/loc-gate.yml" "LOC Gate Rule Pack"

echo "--> 5. Validating Cursor Governance Rules..."
check_file ".cursor/rules/normative-session-flow.mdc" "Normative Session Flow"
check_file ".cursor/rules/graphify.mdc" "Graphify MDC Rule"
check_file ".cursor/rules/bmad-workspace-outputs.mdc" "BMad Workspace Outputs MDC Rule"

echo "============================================="
if [ "$FAILS" -eq 0 ]; then
  echo "🛡️ Platinum Governance Check: 100% COMPLIANT (PASSED)"
  exit 0
else
  echo "❌ Platinum Governance Check: FAILED ($FAILS missing requirements)"
  exit 1
fi
