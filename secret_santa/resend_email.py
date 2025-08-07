"""Resend email sender implementation."""

import os
import resend
from dotenv import load_dotenv
from secret_santa.email_interface import EmailInterface


class ResendEmailSender(EmailInterface):
    """Resend implementation of email interface"""

    def __init__(self):
        load_dotenv()
        resend.api_key = os.environ.get("RESEND_API_KEY")
        self.from_email = os.environ.get("FROM_EMAIL")

    def send_email(self, recipient_email, msg):
        resend.Emails.send(
            {
                "from": self.from_email,
                "to": recipient_email,
                "subject": "Your secret santa info",
                "html": msg,
            }
        )
