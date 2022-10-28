from dotenv import load_dotenv
import smtplib
import os

from . import UserAuth

load_dotenv()


def send_reset_pwd_mail(email: str, link: str) -> None:
    """Sends User Reset Password Mail

    Args:
        Email: User Email ID
        Link: Link to reset password

    Returns:
        None
    """
    MAILGUN_EMAIL = os.getenv('MAILGUN_EMAIL')
    MAILGUN_PWD = os.getenv('MAILGUN_PWD')

    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.login(MAILGUN_EMAIL, MAILGUN_PWD)

    verif_code = UserAuth.add_verif_code(email, 0)

    subject = "JTVMusicApp: Reset Your Password"
    body = f"Dear User \n\nPlease Click on the Link Below to Reset your JTVMusicApp Password for your {email} account. \n\nThis is your 6 Digit Verification Code: {verif_code} \n\nReset Link: {link} \n\nIf you DID NOT ask to reset your password please IGNORE this email!\n\nThank you! \n\nWarm Regards, \n\nThe Help Team \nJTVMusicApp"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(MAILGUN_EMAIL, email, msg)
    server.quit()
