import time

from playsound import playsound
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from macro_class import MacroClass


WAIT_TIME = 1000
STOCK_CHECK_REFRESH_TIME = 15
MAX_STOCK_CHECK = 100


class SSGMacro(MacroClass):
    def __init__(self,
                 website_name: str,
                 login_url: str,
                 item_url: str,
                 login_id: str,
                 login_pw: str):
        super().__init__(website_name, login_url, item_url, login_id, login_pw)

    # override
    def login(self):
        print(f'Logging in {self.website_name}...')
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, "//div/input[@name='mbrLoginId']"))).send_keys(self.login_id)
        self.driver.find_element_by_xpath("//div/input[@name='password']").send_keys(self.login_pw)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//div/button[contains(@class, 'cmem_btn') and contains(@class, 'cmem_btn_ornge')]").click()
        print(f'Successfully logged in {self.website_name}...')

    def check_stock(self, counter):
        print(f'{self.website_name} stock check #{counter}')
        body_text = self.driver.find_element_by_tag_name('body').text
        if '품절' in body_text:
            print('out of stock')
            return True

        print('Has stock!!!!!!')
        return False

    def run(self):
        print(f'Start process for {self.website_name}...')

        self.driver.get(self.login_url)
        self.login()

        self.driver.get(self.item_url)
        assert "[닌텐도 스위치] 모여봐요 동물의 숲 에디션" in self.driver.title

        counter = 1
        while self.check_stock(counter):
            counter += 1
            time.sleep(STOCK_CHECK_REFRESH_TIME)
            if counter > MAX_STOCK_CHECK != -1:
                break
            self.driver.get(self.item_url)
        print(f'{self.item_url}')
        playsound('alarm.mp3')
        time.sleep(10)
        self.driver.close()



