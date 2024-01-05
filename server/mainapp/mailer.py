import os
import smtplib

from dotenv import load_dotenv

load_dotenv()


def send_feedback_mail(
    email: str = "nv9824@srmist.edu.in",
    name: str = "Test User",
    message: str = "Test Message",
) -> None:
    """Sends Feedback Mail To User & Admin

    Args:
        Email: User Email ID
        Name: Name Of User
        Message: User Feedback Message

    Returns:
        None
    """
    MAILGUN_EMAIL = os.getenv("MAILGUN_EMAIL")
    MAILGUN_PWD = os.getenv("MAILGUN_PWD")

    server = smtplib.SMTP("smtp.mailgun.org", 587)
    server.login(MAILGUN_EMAIL, MAILGUN_PWD)

    # User mail subject, body and format of the mail - FROM ADMIN TO USER
    subject1 = "JTVMusicApp: Query/Feedback Received"
    body1 = f"Dear {name} \n\nThank you for reaching out to us! \n\nYour Query/Feedback has been received successfully! \n\nPlease wait until we process the information and get back to you. \n\nHope you have a wonderful day! \n\nWarm Regards, \n\nThe Help Team \nJTVMusicApp"
    msg1 = f"Subject: {subject1}\n\n{body1}"

    # User mail subject, body and format of the mail - FROM WEBSITE TO ADMIN
    subject2 = "JTVMusicApp: Query/Feedback Generated"
    body2 = f"Dear Admin \n\n{name} has generated the following query/feedback \n\nQUERY/FEEDBACK: {message}\n\nPlease get in touch with the user and respond accordingly\n\nThank you! \n\nWarm Regards, \n\nThe Help Team \nJTVMusicApp"
    msg2 = f"Subject: {subject2}\n\n{body2}"

    server.sendmail(MAILGUN_EMAIL, email, msg1)
    server.sendmail(email, MAILGUN_EMAIL, msg2)
    server.quit()


if __name__ == "__main__":
    send_feedback_mail()
