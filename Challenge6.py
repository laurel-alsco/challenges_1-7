# Author: Laurel Miller
import unittest
from selenium import webdriver
from Challenges.Framework.Filters import Filters
from Challenges.Framework.Search import Searches
from Challenges.Framework.screenshot import Screenshot


class Challenge6(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        assert 'Auto Auction', self.driver.title
        self.driver.maximize_window()

    def search_car_negative(self):
        driver = self.driver
        search = Searches(driver)
        filter = Filters(driver)
        search.find_car('honda')
        filter.choosing_filter('Model', 'skyline')

    def search_car_positive(self):
        driver = self.driver
        search = Searches(driver)
        filter = Filters(driver)
        search.find_car('nissan')
        filter.choosing_filter('Model', 'skyline')

    def view_screenshot(self):
        # driver = self.driver
        screenshootin = Screenshot(self.driver, 'No_Filter')
        screenshootin.open_screenshot()


    if __name__ == '__main__':
        unittest.main()









# go to site
# search for nissan with model of skyline
# take screenshot upon getting exception








#
#
# import time
# import unittest
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from Challenges.Screenshot_2 import Screenshot
#
#
# class Challenge6(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome('C:\PycharmProjects\src\AlscoMaster\Challenges\chromedriver.exe')
#
#         # self.driver = webdriver.Chrome('../chromedriver.exe')
#         self.driver.get('https://www.copart.com')
#         assert 'Auto Auction', self.driver.title
#         self.driver.maximize_window()
#         driver = self.driver
#         self.screenshootin = Screenshot(driver, 'Filter_Errors')
#
#     def find_car(self, make):
#         wait = WebDriverWait(self.driver, 200)
#         search = self.driver.find_element_by_id('input-search')
#         search.send_keys(make)
#         for button in self.driver.find_elements_by_xpath('//*[@id="search-form"]//button[@type = "submit" and @ng-click = "search()"]'):
#             button.click()
#             wait.until(EC.presence_of_element_located((By.XPATH, '//tbody//tr')))
#
#     def find_model(self, filter_choice,  model):
#         wait = WebDriverWait(self.driver, 200)
#         model_button = self.driver.find_element_by_xpath('//h4//a[text() = ' + str('\"' + filter_choice.capitalize() + '\"') + ']//i')
#         model_button.click()
#         for filter_input in self.driver.find_elements_by_xpath('//*[@id="collapseinside4"]/form/div/input'):
#             filter_input.click()
#             filter_input.send_keys(model)
#             filter_input.send_keys(Keys.ENTER)
#             wait.until(EC.presence_of_element_located((By.XPATH, '//tbody//tr')))
#             time.sleep(1)
#         try:
#             checkbox = self.driver.find_element_by_xpath(
#                 '//*[@type = "checkbox" and @value= ' + str('\"' + model.capitalize() + '\"') + ']')
#             checkbox.click()
#             time.sleep(2)
#             for car_list in self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable"]//a[@data-uname="lotsearchLotnumber"]'):
#                 car_list.click()
#                 time.sleep(2)
#         except:
#             self.screenshootin.screenshot()
#         finally:
#             self.driver.close()
#
#     def test_search_car_negative(self):
#         self.find_car('honda')
#         self.find_model('Model', 'skyline')
#
#     def test_search_car_positive(self):
#         self.find_car('nissan')
#         self.find_model('Model', 'skyline')
#
#     def test_view_screenshot(self):
#         self.screenshootin.open_screenshot()
#
#     if __name__ == '__main__':
#         unittest.main()
#
#
#
#
#
#
#
#
#
# # go to site
# # search for nissan with model of skyline
# # take screenshot upon getting exception
#
#
#
#
#
#
#
#
# # # Author: Laurel Miller
# # # 10/22/2019
# #
# # import time
# # from selenium import webdriver
# # import os
# # from Challenges.Challenge_6.screenshot import screenshot as s
# # from selenium.webdriver.common.keys import Keys
# # import unittest
# #
# # class Challenge6(unittest.TestCase):
# #     def setUp(self):
# #         # This section will get the copart website and maximize the window.
# #         self.driver = webdriver.Chrome('C:\PycharmProjects\src\AlscoMaster\Challenges\chromedriver.exe')
# #         self.driver.get('https://www.copart.com')
# #         assert'Auto Auction', self.driver.title
# #         self.driver.maximize_window()
# #
# #     #  This function requires a make and a model.
# #     def get_cars(self, make, model):
# #         # This section will input the make into the search field click the search button.
# #         search = self.driver.find_element_by_id('input-search')
# #         search.send_keys(make.upper())
# #         for b in self.driver.find_elements_by_xpath('//*[@id="search-form"]/div/div[2]/button'):
# #             b.click()
# #         assert 'Can not find search field' not in self.driver.page_source
# #         time.sleep(5)
# #         # This function will input the car model into the filter fields section
# #         for btn in self.driver.find_elements_by_xpath('//*[@id="filters-collapse-1"]/div[1]/ul/li[4]/h4/a[1]/i'):
# #             btn.click()
# #         for search in self.driver.find_elements_by_xpath('//*[@id="collapseinside4"]/form/div/input'):
# #             search.send_keys(model)
# #             search.send_keys(Keys.ENTER)
# #             time.sleep(3)
# #         #  This section will check to see if the desired model is available. If it is, it will click on the link.
# #         #  if not, it will take a screenshot of the current screen
# #         try:
# #             checkbox = self.driver.find_element_by_xpath('//*[@id="collapseinside4"]/ul/li[1]/div/label/abbr')
# #             checkbox.click()
# #             # time.sleep(2)
# #         except:
# #             s('no button')
# #     def test_challenge6(self):
# #         # negative test
# #         self.get_cars('nissan', 'gobbly-goop')
# #     def test_positive_challenge6(self):
# #         self.get_cars('nissan', 'skyline')
# #
# #     def tearDown(self):
# #         self.driver.close()
# # if __name__ == '__main__':
# #     unittest.main()
