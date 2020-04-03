from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class MacroClass:
    def __init__(self,
                 website_name: str,
                 login_url: str,
                 item_url: str,
                 login_id: str,
                 login_pw: str):
        self.driver = self.get_driver()
        self.website_name = website_name
        self.login_url = login_url
        self.item_url = item_url
        self.login_id = login_id
        self.login_pw = login_pw

    def get_driver(self):
        driver = webdriver.Chrome()
        driver.wait = WebDriverWait(driver, 2)
        return driver

    def login(self):
        pass

    def check_stock(self, counter):
        pass

    def main(self):
        pass
