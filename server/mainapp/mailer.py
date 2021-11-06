from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


def send_feedback_mail(email: str, name: str, message: str):
    backemail_add = os.getenv('BACKEND_MAIL_ADDR')
    backemail_pwd = os.getenv('BACKEND_MAIL_PWD')

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(backemail_add, backemail_pwd)

    # User mail subject, body and format of the mail - FROM ADMIN TO USER
    subject1 = "MusicApp: Query/Feedback Received"
    body1 = f"Dear {name} \n\nThank you for reaching out to us! \n\nYour Query/Feedback has been received successfully! \n\nPlease wait until we process the information and get back to you. \n\nHope you have a wonderful day! \n\nWarm Regards, \n\nThe Help Team \nMusicApp"
    msg1 = f"Subject: {subject1}\n\n{body1}"

    # User mail subject, body and format of the mail - FROM WEBSITE TO ADMIN
    subject2 = "MusicApp: Query/Feedback Generated"
    body2 = f"Dear Admin \n\n{name} has generated the following query/feedback \n\nQUERY/FEEDBACK: {message}\n\nPlease get in touch with the user and respond accordingly\n\nThank you! \n\nWarm Regards, \n\nThe Help Team \nMusicApp"
    msg2 = f"Subject: {subject2}\n\n{body2}"

    # Sends the mail with the data and quits the server
    server.sendmail(backemail_add, email, msg1)
    server.sendmail(email, backemail_add, msg2)
    print("MAIL SENT SUCCESSFULLY")
    server.quit()
