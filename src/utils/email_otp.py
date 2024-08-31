import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_email(receiver_email: str, otp: int):
    try:
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your OTP Code"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"Your OTP code is {otp}. It is valid for 10 minutes."
        part = MIMEText(text, "plain")
        message.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
