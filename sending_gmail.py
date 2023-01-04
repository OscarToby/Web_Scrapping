import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('Gmail_Python_WebScrapping')
EMAIL_PW = os.environ.get('Gmail_Python_PW')

msg = EmailMessage()
msg['Subject'] = 'Python Developer Jobs'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Python jobs for Alex')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PW)

    smtp.send_message(msg)