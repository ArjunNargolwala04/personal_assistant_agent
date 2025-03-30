import json

def schedule_event(input_data: str) -> str:
    """
    Schedules a calendar event.
    Expects input_data as a JSON string with keys: title, date, time, description, and location.
    """
    try:
        data = json.loads(input_data)
        title = data.get("title")
        date = data.get("date")
        time = data.get("time")
        description = data.get("description", "")
        location = data.get("location", "")

        if not title or not date or not time:
            return "Missing required fields: title, date, and time are required."

        # Here you would integrate with a calendar API (like Google Calendar).
        # For demonstration, we return a simulated success message.
        return (
            f"Event '{title}' scheduled on {date} at {time} "
            f"at {location}. Description: {description}"
        )
    except Exception as e:
        return f"Error scheduling event: {str(e)}"
