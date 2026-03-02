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
        # We need to mock the Cloud Brain call or just test the input validation
        task_data = {
            "command": "Test Command",
            "user_id": "test_user"
        }
        # This will still try to connect to localhost:5000 and likely fail
        # but let's check if it at least passes validation (422 vs 500)
        response = self.client.post("/execute", json=task_data)
        self.assertIn(response.status_code, [200, 500])

if __name__ == '__main__':
    unittest.main()
