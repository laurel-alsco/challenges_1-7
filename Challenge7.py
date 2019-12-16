# Author: Laurel Miller
# 10/24/2019

import time
from Challenges.Framework.screenshot import Screenshot as s
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest

class Challenge7(unittest.TestCase):
    def setUp(self):
        # This function will get the copart website and maximize the window.
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert'Auto Auction', self.driver.title
        self.driver.maximize_window()

    def find_make_and_model(self):
        div = 1
        count = 1
        while div < 5:
            num = 1
            while num < 6:
                cars = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(div) + ']/ul/li[' + str(num) + ']'
                wait = WebDriverWait(self.driver, 200)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabTrending"]')))
                for c in self.driver.find_elements_by_xpath(cars):
                    c.click()
                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="serverSideDataTable"]/tbody')))
                search = '//*[@id="mainBody"]/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/h1/span[1]'
                time.sleep(1)
                if EC.text_to_be_present_in_element(search, 'Search Results'):
                    print('Page', count, 'verified')
                    count +=1
                else:
                    s(self.driver, 'Oops')
                self.driver.back()
                self.driver.back()
                time.sleep(1)

                num +=1
            div += 1

    def test_challenge7(self):
        self.find_make_and_model()
    def tearDown(self):
       self.driver.close()


if __name__ == '__main__':
    unittest.main()





