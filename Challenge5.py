# Author: Laurel Miller
import unittest
from selenium import webdriver
from Challenges.Framework.Filters import Filters
from Challenges.Framework.Search import Searches
from Challenges.Framework.Table_Data import GrabData


class Copart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert'Auto Auction', self.driver.title
        self.driver.maximize_window()

    def test_challenge5(self):
        driver = self.driver
        filters = Filters(driver)
        search = Searches(driver)
        find = GrabData(driver)
        search.find_car('Porsche')
        filters.sort_table_length('1')
        find.damages_count()
        find.models_count()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()


