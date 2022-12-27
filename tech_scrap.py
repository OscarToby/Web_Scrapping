from bs4 import BeautifulSoup
import requests
from itertools import islice
import time

def find_mx_keys():
    ozbargain_mx_keys_text = requests.get('https://www.ozbargain.com.au/product/logitech-mx-keys').text
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
        find_mx_keys()
        time_wait = 10
        print(f'Waiting one hour...')
        time.sleep(time_wait * 600)
