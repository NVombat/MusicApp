from dotenv import load_dotenv
import smtplib
import os

from . import UserAuth

load_dotenv()


def send_reset_pwd_mail(email: str) -> None:
    """Sends User Reset Password Mail

    Args:
        Email: User Email ID

    Returns:
        None
    """
    backemail_add = os.getenv("BACKEND_MAIL_ADDR")
    backemail_pwd = os.getenv("BACKEND_MAIL_PWD")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(backemail_add, backemail_pwd)

    verif_code = UserAuth.add_verif_code(email, 0)

    url = "http://localhost:8000/resetpwd"

    # User mail subject, body and format of the mail
    subject = "JTVMusicApp: Reset Your Password"
    body = f"Dear User \n\nPlease Click on the Link Below to Reset your JTVMusicApp Password for your {email} account. \n\nThis is your 6 Digit Verification Code: {verif_code} \n\nReset Link: {url} \n\nIf you DID NOT ask to reset your password please IGNORE this email!\n\nThank you! \n\nWarm Regards, \n\nThe Help Team \nJTVMusicApp"
    msg = f"Subject: {subject}\n\n{body}"

    # Sends the mail with the data and quits the server
    server.sendmail(backemail_add, email, msg)
    server.quit()
