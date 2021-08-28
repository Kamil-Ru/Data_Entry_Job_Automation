from selenium import webdriver
import time

chrome_driver_path = "C:\Chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


URL_zillow = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22west%22%3A-122.63932265234375%2C%22east%22%3A-122.22733534765625%2C%22south%22" \
             "%3A37.54862360212636%2C%22north%22%3A38.00126648128239%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22" \
             "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1" \
             "%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C" \
             "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B" \
             "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D "

driver.get(URL_zillow)

"""
list_of_offers = driver.find_elements_by_xpath("//article[@class='list-card list-card-additional-attribution list-card_not-saved']")
print(type(list_of_offers))
print(list_of_offers)

price = []

for element in list_of_offers:
    text = element.find_element_by_xpath("//div[@class='list-card-price']").text
    print(text)

"""

test = driver.find_element_by_xpath("//ul[@class='photo-cards photo-cards_wow photo-cards_short']")
print(test)
list_prize = test.find_elements_by_xpath("//div[@class='list-card-price']")
print(len(list_prize))
list_addresses = test.find_elements_by_xpath("//address[@class='list-card-addr']")

test.get_attribute('href')

links = test.find_elements_by_xpath("//a[@class='list-card-link list-card-link-top-margin']")


for link in links:
    print(link.text)

list_of_links = [link.get_attribute('href') for link in links]


print(len(links))



price = []
for element in list_prize:
    text = element.text
    print(text)

addresses = []
for address in list_addresses:
    text = address.text
    print(text)

for link in list_of_links:
    print(link)


