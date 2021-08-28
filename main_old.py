from bs4 import BeautifulSoup
import requests
import pprint

URL_zillow = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22west%22%3A-122.63932265234375%2C%22east%22%3A-122.22733534765625%2C%22south%22" \
             "%3A37.54862360212636%2C%22north%22%3A38.00126648128239%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22" \
             "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1" \
             "%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C" \
             "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B" \
             "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D "
HEADERS = {
  "args": {},
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6127edb7-5f2915847e4fec6263d88e8f"
  },
  "origin": "89.64.57.239",
  "url": "http://httpbin.org/get"
}

import requests

import requests
bot = requests.session()
cookies = bot.get(URL_zillow)

print(cookies)

response = requests.get(URL_zillow, headers=HEADERS, cookies=cookies)



zillow_page = response.text


soup = BeautifulSoup(zillow_page, "html.parser")

print(soup)

offers_list = soup.find_all(name="li")


print(offers_list)

for offer in offers_list:

    url = offer.find(name="a", class_="list-card-link list-card-link-top-margin")
    print(url)
    address = offer.find(name="address", class_="list-card-addr")
    print(address)
    price = offer.find(name="div", class_="list-card-price")
    print(price)

