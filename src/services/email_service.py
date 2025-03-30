import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(input_data: str) -> str:
    """
    Sends an email.
    Expects input_data as a JSON string with keys: recipient, subject, and body.
    """
    try:
        # Parse the input JSON string.
        data = json.loads(input_data)
        recipient = data.get("recipient")
        subject = data.get("subject")
        body = data.get("body")

        if not recipient or not subject or not body:
            return "Missing recipient, subject, or body in input."

        # Email server configuration.
        host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        port = int(os.getenv("EMAIL_PORT", "587"))
        username = os.getenv("EMAIL_HOST_USER")
        password = os.getenv("EMAIL_HOST_PASSWORD")

        if not username or not password:
            return "Email credentials are not set in environment variables."

        # Set up the email message.
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the server and send the email.
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, recipient, msg.as_string())
        server.quit()

        return f"Email sent to {recipient}."
    except Exception as e:
        return f"Error sending email: {str(e)}"
