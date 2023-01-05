import smtplib
from email.message import EmailMessage
import os

def send(user_email, subject, message):
    host_email = "daveendev07@gmail.com"
    receiver_email = "daveduran07@gmail.com"
    password = os.getenv("SENDMAIL-PASSWORD")

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    print(password)
    s.login(host_email, password)

    s.sendmail(host_email, receiver_email, message)
    s.quit()


if __name__ == "__main__":
    send("daveduran07@gmail.com", "Test email", "This is a test email")