# Author: Laurel Miller
# 10/3/2019

import time
from selenium import webdriver
import unittest

class Challenge2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.maximize_window()

    def get_page(self):
        self.driver.get('https://www.copart.com')
        assert 'Auto Auction', self.driver.title
        search = self.driver.find_element_by_id('input-search')
        search.send_keys('exotics')
        for button in self.driver.find_elements_by_xpath('//button[@type="submit" and @ng-click = "search()"]'):
            button.click()
        assert 'Can not find search field' not in self.driver.page_source
        time.sleep(4)

    def row_data(self):

        table = self.driver.find_element_by_xpath('//table//tbody//tr')
        assert 'no such name' not in self.driver.page_source
        row_number = 0
        while row_number < 10:
            row = table.find_elements_by_xpath('//tr[' + str(row_number) + ']/td')
            rData = []
            for text in row:
                rData.append(text.text)
            row_number += 1
            return rData

    def column_data(self, make):
        table = self.driver.find_elements_by_xpath('//td//span[@data-uname = "lotsearchLotmake"]')
        assert 'no such name' not in self.driver.page_source
        rData = []
        for car in table:
            rData.append(car.text)
        assert make in rData, 'The desired make: \'' + make.title() + '\' is not on the list of Exotic cars.'
        print('The requested make \'' + make + '\' is in the list of Exotic cars.')

    def test_challenge2(self):
        self.get_page()
        self.row_data()
        self.column_data('Porsche'.upper())

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()



