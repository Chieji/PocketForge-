import unittest
from fastapi.testclient import TestClient
from local_executor.main import app

class TestLocalExecutor(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_status(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "idle"})

    def test_execute_task(self):
        task_data = {
            "task": "Test Task",
            "steps": [{"action": "navigate", "url": "http://example.com"}]
        }
        response = self.client.post("/execute", json=task_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())
        self.assertEqual(response.json()["task"], "Test Task")

if __name__ == '__main__':
    unittest.main()
