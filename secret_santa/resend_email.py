import resend
from dotenv import load_dotenv
import os
from secret_santa.email_interface import EmailInterface

load_dotenv()

API_KEY = os.environ.get("RESEND_API_KEY")
print(API_KEY)
resend.api_key = API_KEY

# resend.api_key = "re_RqJZr6m6_968A43q6St6zDsBamvhp4FCM"


class ResendEmailSender(EmailInterface):
    """Resend implementation of email interface"""

    def __init__(self):
        load_dotenv()
        resend.api_key = os.environ.get("RESEND_API_KEY")

    def send_email(self, recipient_email, msg):
        resend.Emails.send(
            {
                "from": "hello@secretsanta.helenffion.cafe",
                "to": recipient_email,
                "subject": "Your secret santa info",
                "html": msg,
            }
        )
