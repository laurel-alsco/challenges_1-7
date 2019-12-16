# # Author: Laurel Miller
# # 10/10/2019
import unittest
from selenium import webdriver

class PopularItems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('https://www.copart.com')
        assert 'Auto Auction', self.driver.title
        self.driver.maximize_window()

    # This function will get a list of cars from the copart most popular items makes/models section on the homepage
    def test_get_cars(self):
        cars = self.driver.find_elements_by_xpath('//div[@class = "row"]//li[contains(@ng-repeat, "popularSearch")]//a')
        i = 0
        while i in range(len(cars)):
            for car in cars:
                car_url = car.get_attribute('href')
                print(car.text, '-', car_url)
                i += 1

    def tear_down(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()










# from selenium import webdriver



# import unittest
# # This class is for Challenge 3 this section finds the copart website
# class Challenge3(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome('C:\PycharmProjects\src\AlscoMaster\Challenges\chromedriver.exe')
#         self.driver.get('https://www.copart.com')
#         assert 'Auto Auction', self.driver.title
#
#     # This function will get a list of cars from the copart most popular items makes/models section on the homepage
#     def get_cars(self):
#         div = 1
#         while div < 5:
#             num = 1
#             while num < 6:
#                 cars = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(div) + ']/ul/li[' + str(num) + ']'
#                 urls = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(div) + ']/ul/li[' + str(num) + ']/a[@href]'
#                 for car in (el.text for el in (self.driver.find_elements_by_xpath(cars))):
#                     for elem in (self.driver.find_elements_by_xpath(urls)):
#                         url = elem.get_attribute('href')
#                         num += 1
#                         print(car, '-', url)
#             div += 1
#     def test_challenge3(self):
#         self.get_cars()
#
#     def tearDown(self):
#         self.driver.close()
#
#
#
#
