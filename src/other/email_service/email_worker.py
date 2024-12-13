import smtplib
from src.configs import EmailConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailWorker:
    smtp_server = smtplib.SMTP("smtp.list.ru", 587)
    smtp_server.starttls()
    smtp_server.login(EmailConfig.EMAIL_URL, EmailConfig.EMAIL_PASSWORD)

    @classmethod
    def send_message(cls, url_update: str, email_user: str) -> None:
        message = MIMEMultipart()
        message["From"] = EmailConfig.EMAIL_URL
        message["To"] = email_user
        message["Subject"] = EmailConfig.EMAIL_HEADER

        message.attach(MIMEText(url_update, "plain"))

        cls.smtp_server.sendmail(EmailConfig.EMAIL_URL, email_user, message.as_string())
        cls.smtp_server.close()
