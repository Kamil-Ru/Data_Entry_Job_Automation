from selenium import webdriver
import time
from password import ZILLOW_URL
from selenium.webdriver.common.keys import Keys


class Zillow:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver")
        self.driver.get(ZILLOW_URL)
        time.sleep(1)

    def get_data(self):
        # Loading page
        html = self.driver.find_element_by_tag_name('html')
        for _ in range(10):
            html.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        # Getting list of cards
        list_of_cards = self.driver.find_elements_by_xpath(
            "//article[@class='list-card list-card-additional-attribution list-card_not-saved']")

        # Creating Json with data
        data = {}
        a = 0
        for card in list_of_cards:
            prize = card.find_element_by_xpath(".//div[@class='list-card-price']").text
            address = card.find_element_by_xpath(".//address[@class='list-card-addr']").text
            link = card.find_element_by_xpath(".//a[@class='list-card-link list-card-link-top-margin']").get_attribute(
                'href')
            data[str(a)] = {"Address": address, "Prize": prize, "URL": link}
            a = a + 1

        self.driver.close()
        return data
