import os
import shutil
import sys

REQUESTED_SKILLS = [
    # Section 8A — BMad core / workflow
    'bmad-help', 'bmad-dev-story', 'bmad-create-story', 'bmad-quick-dev', 'bmad-code-review',
    'bmad-checkpoint-preview', 'bmad-correct-course', 'bmad-sprint-planning', 'bmad-sprint-status',
    'bmad-retrospective', 'bmad-check-implementation-readiness', 'bmad-create-prd', 'bmad-edit-prd',
    'bmad-validate-prd', 'bmad-create-epics-and-stories', 'bmad-create-architecture',
    'bmad-create-ux-design', 'bmad-generate-project-context', 'bmad-document-project',
    'bmad-index-docs', 'bmad-technical-research', 'bmad-domain-research', 'bmad-market-research',
    'bmad-product-brief', 'bmad-prfaq', 'bmad-distillator', 'bmad-shard-doc',
    'bmad-review-adversarial-general', 'bmad-review-edge-case-hunter', 'bmad-advanced-elicitation',
    'bmad-brainstorming', 'bmad-party-mode', 'bmad-erpnext-expert',
    # Section 8B — Platinum (Rock)
    'bmad-platinum-story-delivery', 'bmad-agent-rock', 'bmad-agent-john',
    # Section 8C — TEA (Test Architect Enterprise)
    'bmad-tea', 'bmad-teach-me-testing', 'bmad-testarch-trace', 'bmad-testarch-nfr',
    'bmad-testarch-atdd', 'bmad-testarch-automate', 'bmad-testarch-test-review',
    'bmad-testarch-test-design', 'bmad-testarch-framework', 'bmad-testarch-ci',
    'bmad-qa-generate-e2e-tests',
    # Section 8D — CIS (methods + coaches)
    'bmad-cis-innovation-strategy', 'bmad-cis-problem-solving', 'bmad-cis-design-thinking',
    'bmad-cis-storytelling', 'bmad-cis-agent-brainstorming-coach', 'bmad-cis-agent-creative-problem-solver',
    'bmad-cis-agent-design-thinking-coach', 'bmad-cis-agent-innovation-strategist',
    'bmad-cis-agent-presentation-master', 'bmad-cis-agent-storyteller',
    # Section 8E — Graphify
    'bmad-graphify', 'bmad-graphify-query', 'bmad-graphify-path', 'bmad-graphify-explain',
    'dontbmad-graphify',
    # Section 8F — dontbmad acceleration
    'dontbmad-compress-artifacts', 'dontbmad-caveman', 'dontbmad-grill', 'dontbmad-auto-sprint',
    'dontbmad-claude-design-to-bmad-uiux', 'dontbmad-bmad-to-claude-design',
    # Section 8G — Frappe platform skills
    'frappe-platform-operations', 'frappe-code-ql', 'frappe-whitelisted-api', 'frappe-desk-js-quality',
    'frappe-uam-client-enabled-sync', 'frappe-iam-adapter-patterns', 'frappe-iam-audit-program',
    'frappe-fpatch-platform-patterns', 'frappe-agentix-crewai-patterns',
    'frappe-app-radar-security-patterns', 'frappe-trishul-devops-patterns',
    'latte-dlp-before-insert-script', 'frappe-bmad-setup', 'figma-make-kodosh-b2b',
    # Section 8H — Platform governance skills
    'platform-quality-guidelines', 'platform-security-review'
]

REPO_ROOT = '/Users/devang/Desktop/Future_Ready_Hackathon'
HOME = os.path.expanduser('~')

TARGET_DIRS = [
    os.path.join(REPO_ROOT, '.claude', 'skills'),
    os.path.join(REPO_ROOT, '.cursor', 'skills'),
    os.path.join(REPO_ROOT, '.agents', 'skills'),
    os.path.join(REPO_ROOT, '.gemini', 'skills'),
    os.path.join(HOME, '.claude', 'skills'),
    os.path.join(HOME, '.cursor', 'skills'),
    os.path.join(HOME, '.gemini', 'skills'),
]

SOURCE_DIR = os.path.join(REPO_ROOT, 'dont-b-mad', 'claude', 'skills')

def parse_frontmatter(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
    if not content.startswith('---'):
        return None, None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, None
    fm = parts[1]
    name, desc = None, None
    for line in fm.split('\n'):
        if line.startswith('name:'):
            name = line.split(':', 1)[1].strip().strip('\'"')
        elif line.startswith('description:'):
            desc = line.split(':', 1)[1].strip().strip('\'"')
    return name, desc

def deploy_skills():
    print(f"Deploying skills from source: {SOURCE_DIR}")
    all_source_skills = [d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))]
    print(f"Total skills available in source: {len(all_source_skills)}")
    
    # Verify all requested are in source
    missing_in_source = [r for r in REQUESTED_SKILLS if r not in all_source_skills]
    if missing_in_source:
        print(f"ERROR: Missing in source: {missing_in_source}")
        sys.exit(1)
        
    for target in TARGET_DIRS:
        os.makedirs(target, exist_ok=True)
        deployed_count = 0
        for skill_name in all_source_skills:
            src_skill = os.path.join(SOURCE_DIR, skill_name)
            dst_skill = os.path.join(target, skill_name)
            if os.path.exists(dst_skill) or os.path.islink(dst_skill):
                if os.path.islink(dst_skill):
                    os.unlink(dst_skill)
                else:
                    shutil.rmtree(dst_skill)
            shutil.copytree(src_skill, dst_skill)
            deployed_count += 1
        print(f"Deployed {deployed_count} skills to: {target}")

def verify_deployments():
    print("\n--- Verifying Deployments across all 7 Targets ---")
    all_passed = True
    for target in TARGET_DIRS:
        print(f"\nChecking target: {target}")
        if not os.path.isdir(target):
            print(f"  FAILED: Target directory does not exist: {target}")
            all_passed = False
            continue
            
        installed = set(os.listdir(target))
        missing = [r for r in REQUESTED_SKILLS if r not in installed]
        if missing:
            print(f"  FAILED: Missing {len(missing)} skills: {missing}")
            all_passed = False
            continue
            
        # Verify each requested skill in target
        for r in REQUESTED_SKILLS:
            skill_md = os.path.join(target, r, 'SKILL.md')
            if not os.path.isfile(skill_md):
                print(f"  FAILED: Missing SKILL.md for {r}")
                all_passed = False
                continue
            name, desc = parse_frontmatter(skill_md)
            if not name or not desc:
                print(f"  FAILED: Invalid frontmatter in {skill_md}")
                all_passed = False
                continue
            if name != r:
                print(f"  FAILED: Frontmatter name mismatch in {skill_md} (got {name}, expected {r})")
                all_passed = False
                continue
            with open(skill_md, 'r', errors='ignore') as f:
                lines = f.readlines()
                if len(lines) > 200:
                    print(f"  FAILED: {skill_md} exceeds 200 LOC ({len(lines)} lines)")
                    all_passed = False
                    continue
        print(f"  PASSED: All {len(REQUESTED_SKILLS)} requested skills verified in {target} (Valid frontmatter & LOC <= 200).")
    
    if all_passed:
        print("\nALL VERIFICATIONS PASSED SUCCESSFULLY (7/7 Targets OK)!")
    else:
        print("\nSOME VERIFICATIONS FAILED!")
        sys.exit(1)

if __name__ == '__main__':
    deploy_skills()
    verify_deployments()
