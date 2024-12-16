import smtplib
from src.configs import EmailConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailWorker:
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(EmailConfig.EMAIL_URL, EmailConfig.EMAIL_PASSWORD)

    @classmethod
    def send_message(cls, url_update: str, email_user: str) -> None:
        """
        Send message in email
        :param url_update:
        :param email_user:
        """

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(EmailConfig.EMAIL_URL, EmailConfig.EMAIL_PASSWORD)  # noqa

            message = MIMEMultipart()
            message["From"] = EmailConfig.EMAIL_URL
            message["To"] = email_user
            message["Subject"] = EmailConfig.EMAIL_HEADER

            message.attach(MIMEText(url_update, "plain"))

            smtp_server.sendmail(
                EmailConfig.EMAIL_URL, email_user, message.as_string()  # noqa
            )  # noqa
