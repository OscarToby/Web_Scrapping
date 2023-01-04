from bs4 import BeautifulSoup
import requests
from itertools import islice
import time
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('Gmail_Python_WebScrapping')
EMAIL_PW = os.environ.get('Gmail_Python_PW')

URL = 'https://www.ozbargain.com.au/product/logitech-mx-keys'

def find_product():
    ozbargain_mx_keys_text = requests.get(URL).text
    soup = BeautifulSoup(ozbargain_mx_keys_text, 'lxml')
    banners = soup.find_all('div', class_ = 'n-right')
    limit = 5

    for index, item in enumerate(islice(banners, limit)):
        product = item.h2.a.text
        date_submitted = item.find('div', class_ = 'submitted').text.split()[-4:-1:2]
        expiry = item.find('span', class_ = 'nodeexpiry').text
        node = item.h2.a['href']
        weblink = f'https://www.ozbargain.com.au{node}'
        print(f'''
        Product:        {product}
        Date Submitted: {date_submitted}
        Expiry:         {expiry.strip()}
        Weblink:        {weblink}''')

if __name__ == '__main__':
    while True:
        find_product()
        time_wait = 10
        print(f'Waiting one hour...')
        time.sleep(time_wait * 600)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PW)

    subject = 'Python Developer Jobs'
    body = find_product()

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)