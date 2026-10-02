from agents import Agent, function_tool, ModelSettings
from messenger import send_email
import os
from dotenv import load_dotenv
load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")

settings = ModelSettings(tool_choice="required")

@function_tool
def send_email_tool(subject: str, text_body: str, html_body: str, to_address: str) -> str:
    """
    Send out an email with the given subject and body to the given recipient

    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
        to_address: The recipient email address
    """
    send_email(subject, text_body, html_body, to_address)
    return "Email sent successfully"


INSTRUCTIONS = """
You are provided with a detailed report and a recipient email address. Use your tool to send an email
to that recipient, converting the report into a clean, well presented HTML email with an appropriate
subject line. Use exactly the recipient address given to you as to_address.
"""

email_agent = Agent(
    name="Email Agent",
    instructions=INSTRUCTIONS,
    tools=[send_email_tool],
    model=MODEL_NAME,
    model_settings=settings,
)