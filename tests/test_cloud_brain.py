import unittest
from cloud_brain.planner import AIPlanner
from cloud_brain.memory import MemoryEngine
from cloud_brain.github_service import GitHubService

class TestCloudBrain(unittest.TestCase):
    def setUp(self):
        self.planner = AIPlanner(api_key="test_key")
        self.memory = MemoryEngine()
        self.github = GitHubService(token="test_token")

    def test_generate_plan_with_code_change(self):
        plan = self.planner.generate_plan("update logic for posts")
        self.assertEqual(plan["task"], "update logic for posts")
        actions = [step["action"] for step in plan["steps"]]
        self.assertIn("code_change", actions)

    def test_github_service_branch(self):
        res = self.github.create_branch("test-branch")
        self.assertEqual(res["status"], "success")

    def test_github_service_commit(self):
        res = self.github.commit_change("test-branch", "file.py", "content", "msg")
        self.assertEqual(res["status"], "success")

    def test_self_improvement_methods(self):
        self.assertEqual(self.planner.review_code("code")["status"], "approved")
        self.assertEqual(self.planner.refactor_code("code"), "code")

if __name__ == '__main__':
    unittest.main()
