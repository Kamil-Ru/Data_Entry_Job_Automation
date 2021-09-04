from selenium import webdriver
import time
from password import GOOGLE_DOCS


class Google_Docs:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver")
        self.driver.get(GOOGLE_DOCS)
        time.sleep(1)

    def send_data(self, address=None, prize=None, url=None):
        searching_cards = self.driver.find_elements_by_xpath("//input[@class='quantumWizTextinputPaperinputInput exportInput']")

        list = [address, prize, url]

        for i in range(len(searching_cards)):
            searching_cards[i].send_keys(list[i])

        send_button = self.driver.find_element_by_xpath(
            "//span[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent']")
        send_button.click()
        time.sleep(1)
        self.driver.quit()





