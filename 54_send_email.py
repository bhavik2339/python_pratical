# 54. Send an Email
import smtplib
from email.message import EmailMessage

sender = "your_email@gmail.com"
app_password = "YOUR_APP_PASSWORD"
receiver = "receiver@example.com"

msg = EmailMessage()
msg["Subject"] = "Test Email from Python"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Hello! This email was sent using Python.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, app_password)
    smtp.send_message(msg)

print("Email sent successfully.")
