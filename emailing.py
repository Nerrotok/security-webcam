import smtplib
import imghdr
from email.message import EmailMessage
import config

password = config.password
email_sender = config.password
email_receiver = config.password


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Should they be here?"
    email_message.set_content("Hey, we spotted something!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_sender, password)
    gmail.sendmail(email_sender, email_receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email()
