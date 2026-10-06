from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List




conf = ConnectionConfig(
    MAIL_USERNAME = "harshsaini7875@gmail.com",
    MAIL_PASSWORD = "uvle zoiv pxjf kxzt",
    MAIL_FROM = "harshsaini7875@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Todo Application",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)






async def send_email(emails:List[str]):
    html = """<p>Hi, Thanks for registration l</p> """

    message = MessageSchema(
        subject="Registration Confirm ",
        recipients= emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return {
        "message": "email has been sent"
    }
    # print({"message": "email has been sent"})