from abc import ABC, abstractmethod


class EmailInterface(ABC):
    """Send an email with content msg to the recipient."""

    @abstractmethod
    def send_email(self, recipient_email, msg):
        """Send an email with content msg to the recipient."""
