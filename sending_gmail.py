import os
import smtplib

EMAIL_ADDRESS = os.environ.get('Gmail_Python_WebScrapping')
EMAIL_PW = os.environ.get('Gmail_Python_PW')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PW)

    subject = 'Python Developer Jobs'
    body = 'Python jobs for Alex'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'au.alex5@gmail.com', msg)