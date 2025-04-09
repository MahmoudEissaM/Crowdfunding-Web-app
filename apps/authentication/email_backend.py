from django.core.mail.backends.smtp import EmailBackend
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings

class CustomEmailBackend(EmailBackend):
    def open(self):
        """
        Ensures we have a connection to the email server. Returns whether or
        not a new connection was required (True or False).
        """
        if self.connection:
            # Nothing to do if the connection is already open.
            return False

        try:
            # If local_hostname is not specified, socket.getfqdn() gets used.
            # For performance, skip the hostname check of fqdn.
            self.connection = smtplib.SMTP(
                self.host, self.port,
                local_hostname=None,
                timeout=self.timeout
            )
            if self.use_tls:
                self.connection.starttls()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise 