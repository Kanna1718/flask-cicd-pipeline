import unittest
from app.main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "online")
        self.assertEqual(data["version"], "1.0.0")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("timestamp", data)

    def test_add_numbers_success(self):
        payload = {"a": 15, "b": 27}
        response = self.client.post("/api/add", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["result"], 42.0)

    def test_add_numbers_missing_keys(self):
        payload = {"a": 10}
        response = self.client.post("/api/add", json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_add_numbers_invalid_types(self):
        payload = {"a": "invalid", "b": 10}
        response = self.client.post("/api/add", json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
