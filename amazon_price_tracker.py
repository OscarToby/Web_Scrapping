import requests
from bs4 import BeautifulSoup

URL_Bridal_Sunglasses = "https://www.amazon.com.au/Caeedn-Sunglasses-Glasses-Female-Protection/dp/B09MBC4GYR/ref=sr_1_7?crid=3TXAWYEM9YLMN&keywords=white+sunglasses&qid=1678254810&sprefix=white+sunglass%2Caps%2C376&sr=8-7"

URL_Bridal_Gloves = "https://www.amazon.com.au/Acenail-Womens-Wedding-Gloves-Evening/dp/B09SL3ZZK9/ref=sr_1_5?crid=273P3ZVPJ3U6Z&keywords=bridal+gloves&qid=1678254875&sprefix=bridal+glo%2Caps%2C241&sr=8-5"

URL_Bib_Tights = "https://www.amazon.com.au/Santic-Cycling-Tights-Padded-Legging/dp/B07ZYZ52PL/ref=sr_1_17?crid=2LLEWVIUYDCQB&keywords=bib+tights+cycling+men&qid=1678337493&sprefix=bib+tights+c%2Caps%2C353&sr=8-17"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

page = requests.get(URL_Bib_Tights, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="desktop_unifiedPrice").get_text()

print(title.strip())
print(price.strip())