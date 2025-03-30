import unittest
import json
from src.services.calendar_service import schedule_event

class TestCalendarService(unittest.TestCase):
    def test_schedule_event_missing_fields(self):
        # Test when required fields are missing.
        input_data = json.dumps({"title": "Meeting"})
        result = schedule_event(input_data)
        self.assertIn("Missing required fields", result)

    def test_schedule_event_success(self):
        # Test scheduling an event with complete details.
        input_data = json.dumps({
            "title": "Project Meeting",
            "date": "2025-04-01",
            "time": "10:00 AM",
            "description": "Discuss project milestones",
            "location": "Conference Room"
        })
        result = schedule_event(input_data)
        self.assertIn("Event 'Project Meeting' scheduled", result)

if __name__ == "__main__":
    unittest.main()
