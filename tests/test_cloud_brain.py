import unittest
from cloud_brain.planner import AIPlanner
from cloud_brain.memory import MemoryEngine

class TestCloudBrain(unittest.TestCase):
    def setUp(self):
        self.planner = AIPlanner(api_key="test_key")
        self.memory = MemoryEngine()

    def test_generate_plan(self):
        plan = self.planner.generate_plan("Post a photo")
        self.assertEqual(plan["task"], "Post a photo")
        self.assertIn("steps", plan)

    def test_memory_storage(self):
        self.memory.store_event("test_event", {"data": "value"})
        context = self.memory.get_context("test_event")
        self.assertEqual(context["data"], "value")

    def test_style_model(self):
        self.memory.update_style_model("user1", ["sample1", "sample2"])
        style = self.memory.get_style("user1")
        self.assertEqual(style, "professional")

if __name__ == '__main__':
    unittest.main()
