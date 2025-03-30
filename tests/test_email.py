import unittest
import json
from src.services.email_service import send_email

class TestEmailService(unittest.TestCase):
    def test_send_email_missing_fields(self):
        # Test when required fields are missing.
        input_data = json.dumps({"recipient": "test@example.com"})
        result = send_email(input_data)
        self.assertIn("Missing recipient, subject, or body", result)

    def test_send_email_invalid_json(self):
        # Test with invalid JSON input.
        input_data = "not a json"
        result = send_email(input_data)
        self.assertIn("Error sending email", result)

if __name__ == "__main__":
    unittest.main()
