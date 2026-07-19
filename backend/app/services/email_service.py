import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.logging import logger


class EmailService:
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        username: str,
        password: str,
        use_tls: bool = True,
    ):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        html: bool = False,
    ) -> bool:
        try:
            msg = MIMEMultipart()
            msg["From"] = self.username
            msg["To"] = recipient
            msg["Subject"] = subject

            if html:
                msg.attach(MIMEText(body, "html"))
            else:
                msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
            )

            if self.use_tls:
                server.starttls()

            server.login(
                self.username,
                self.password,
            )

            server.sendmail(
                self.username,
                recipient,
                msg.as_string(),
            )

            server.quit()

            logger.info(
                "Email sent successfully to {}",
                recipient,
            )

            return True

        except Exception as e:
            logger.error(
                "Failed to send email: {}",
                str(e),
            )

            return False
