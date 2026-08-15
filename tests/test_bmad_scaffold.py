"""
BMad AI OS Scaffold & Governance Verification Test Suite.
Verifies Section 16 requirements and constitutional invariants.
"""
from pathlib import Path
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent


class TestBMadScaffold(unittest.TestCase):
    """Test suite verifying BMad OS scaffolding and Section 16 gates."""

    def test_bmad_help_csv_exists(self):
        """Verify _bmad/_config/bmad-help.csv exists and has complete routing."""
        help_file = ROOT_DIR / "_bmad" / "_config" / "bmad-help.csv"
        self.assertTrue(help_file.is_file(), "_bmad/_config/bmad-help.csv must exist")
        content = help_file.read_text(encoding="utf-8")
        for skill in [
            "bmad-help", "bmad-prd", "bmad-architecture", "bmad-sprint-planning",
            "bmad-dev-story", "bmad-platinum-story-delivery", "bmad-agent-rock"
        ]:
            self.assertIn(skill, content, f"Routing skill {skill} missing in bmad-help.csv")

    def test_agent_manifest_csv(self):
        """Verify _bmad/_config/agent-manifest.csv includes all required agents."""
        manifest_file = ROOT_DIR / "_bmad" / "_config" / "agent-manifest.csv"
        self.assertTrue(manifest_file.is_file(), "agent-manifest.csv must exist")
        content = manifest_file.read_text(encoding="utf-8")
        for agent in ["bmad-help", "dev", "pm", "architect", "analyst", "tech-writer",
                      "ux-designer", "bmad-tea", "brainstorming", "rock"]:
            self.assertIn(agent, content, f"Agent {agent} must be in agent-manifest.csv")

    def test_team_and_module_configs(self):
        """Verify team.yaml, workspace.yaml, and module config files exist."""
        expected_configs = [
            ROOT_DIR / "_bmad" / "_config" / "team.yaml",
            ROOT_DIR / "_bmad" / "workspace.yaml",
            ROOT_DIR / "_bmad" / "core" / "config.yaml",
            ROOT_DIR / "_bmad" / "bmm" / "config.yaml",
            ROOT_DIR / "_bmad" / "cis" / "config.yaml",
            ROOT_DIR / "_bmad" / "tea" / "config.yaml",
            ROOT_DIR / "_bmad" / "bmb" / "config.yaml",
        ]
        for cfg in expected_configs:
            self.assertTrue(cfg.is_file(), f"Config {cfg.relative_to(ROOT_DIR)} must exist")

    def test_sprint_status_yaml_valid(self):
        """Verify sprint-status.yaml exists and is valid YAML."""
        status_file = ROOT_DIR / "_bmad-output" / "implementation-artifacts" / "sprint-status.yaml"
        self.assertTrue(status_file.is_file(), "sprint-status.yaml must exist")
        content = status_file.read_text(encoding="utf-8")
        try:
            import yaml
            data = yaml.safe_load(content)
            self.assertIsInstance(data, dict)
            self.assertIn("development_status", data)
        except ImportError:
            # Fallback verification without PyYAML dependency
            self.assertIn("development_status:", content)
            self.assertIn("project:", content)

    def test_constitution_article_vi_b(self):
        """Verify .specify/memory/constitution.md exists and contains Article VI-B."""
        const_file = ROOT_DIR / ".specify" / "memory" / "constitution.md"
        self.assertTrue(const_file.is_file(), "constitution.md must exist")
        content = const_file.read_text(encoding="utf-8")
        self.assertIn("Article VI-B", content)
        self.assertIn("Graph-First Retrieval", content)

    def test_agents_md_exists(self):
        """Verify AGENTS.md exists and contains agent roles."""
        agents_file = ROOT_DIR / "AGENTS.md"
        self.assertTrue(agents_file.is_file(), "AGENTS.md must exist")
        content = agents_file.read_text(encoding="utf-8")
        self.assertIn("agent-governance", content)
        self.assertIn("agent-architect", content)

    def test_project_context_md_exists(self):
        """Verify project-context.md exists in root and output."""
        root_ctx = ROOT_DIR / "project-context.md"
        out_ctx = ROOT_DIR / "_bmad-output" / "project-context.md"
        self.assertTrue(root_ctx.is_file(), "project-context.md must exist in root")
        self.assertTrue(out_ctx.is_file(), "project-context.md must exist in _bmad-output")

    def test_claude_skills_exist(self):
        """Verify .claude/skills/ platinum story delivery and agent rock exist."""
        psd_skill = ROOT_DIR / ".claude" / "skills" / "bmad-platinum-story-delivery" / "SKILL.md"
        rock_skill = ROOT_DIR / ".claude" / "skills" / "bmad-agent-rock" / "SKILL.md"
        self.assertTrue(psd_skill.is_file(), "bmad-platinum-story-delivery SKILL.md must exist")
        self.assertTrue(rock_skill.is_file(), "bmad-agent-rock SKILL.md must exist")

    def test_loc_limit_per_file(self):
        """Verify newly created scaffold scripts, configs, docs and tests are <= 200 LOC."""
        scaffold_files = [
            ROOT_DIR / "_bmad" / "_config" / "bmad-help.csv",
            ROOT_DIR / "_bmad" / "_config" / "agent-manifest.csv",
            ROOT_DIR / "_bmad" / "_config" / "team.yaml",
            ROOT_DIR / "_bmad" / "workspace.yaml",
            ROOT_DIR / "_bmad" / "core" / "config.yaml",
            ROOT_DIR / "_bmad" / "bmm" / "config.yaml",
            ROOT_DIR / "_bmad" / "cis" / "config.yaml",
            ROOT_DIR / "_bmad" / "tea" / "config.yaml",
            ROOT_DIR / "_bmad" / "bmb" / "config.yaml",
            ROOT_DIR / "_bmad-output" / "implementation-artifacts" / "sprint-status.yaml",
            ROOT_DIR / "_bmad-output" / "implementation-artifacts" / "templates" / "rock-platinum-session-checkpoint.md",
            ROOT_DIR / "_bmad-output" / "project-context.md",
            ROOT_DIR / "project-context.md",
            ROOT_DIR / ".specify" / "memory" / "constitution.md",
            ROOT_DIR / "AGENTS.md",
            ROOT_DIR / ".claude" / "skills" / "bmad-platinum-story-delivery" / "SKILL.md",
            ROOT_DIR / ".claude" / "skills" / "bmad-agent-rock" / "SKILL.md",
            ROOT_DIR / "tests" / "test_bmad_scaffold.py",
        ]
        violating_files = []
        for file_path in scaffold_files:
            self.assertTrue(file_path.is_file(), f"Expected file {file_path.name} to exist")
            lines = len(file_path.read_text(encoding="utf-8").splitlines())
            if lines > 200:
                violating_files.append((file_path.name, lines))

        self.assertEqual(len(violating_files), 0, f"Files exceeding 200 LOC: {violating_files}")


if __name__ == "__main__":
    unittest.main()
