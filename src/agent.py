import os
from langchain.llms import OpenAI
from langchain.agents import Tool, initialize_agent
from src.services.email_service import send_email
from src.services.calendar_service import schedule_event

# Define the Email tool
email_tool = Tool(
    name="Email",
    func=send_email,
    description=(
        "Send an email. The input should be a JSON string with keys: "
        "'recipient', 'subject', and 'body'."
    )
)

# Define the Calendar tool
calendar_tool = Tool(
    name="Calendar",
    func=schedule_event,
    description=(
        "Schedule a calendar event. The input should be a JSON string with keys: "
        "'title', 'date', 'time', 'description', and 'location'."
    )
)

# Initialize the language model.
# Ensure your OPENAI_API_KEY is set in the environment or in your .env file.
llm = OpenAI(temperature=0)

# List of available tools
tools = [email_tool, calendar_tool]

# Initialize the Langchain agent using a zero-shot-react description framework.
assistant_agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
