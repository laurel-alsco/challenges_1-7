# Author: Laurel Miller
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Challenges.Framework.screenshot import Screenshot


class Filters:
    def __init__(self, driver):
        self.driver = driver

    def choosing_filter(self, filter_choice,  filter_keys):
        wait = WebDriverWait(self.driver, 200)
        model_button = self.driver.find_element_by_xpath('//h4//a[text() = ' + str('\"' + filter_choice.capitalize() + '\"') + ']//i')
        model_button.click()
        for filter_input in self.driver.find_elements_by_xpath('//*[@id="collapseinside4"]/form/div/input'):
            filter_input.click()
            filter_input.send_keys(filter_keys)
            filter_input.send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located((By.XPATH, '//tbody//tr')))
            time.sleep(1)
        try:
            checkbox = self.driver.find_element_by_xpath(
                '//*[@type = "checkbox" and @value= ' + str('\"' + filter_keys.capitalize() + '\"') + ']')
            checkbox.click()
            time.sleep(2)
            for car_list in self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable"]//a[@data-uname="lotsearchLotnumber"]'):
                car_list.click()
                time.sleep(2)
        except:
            Screenshot(self.driver, 'No_Filter').take_screenshot()
        finally:
            self.driver.close()

    def sort_table_length(self, items_visible):
        filter_drop = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable_length"]/label/select')
        for d in filter_drop:
            self.driver.implicitly_wait(5)
            d.click()
            d.send_keys(items_visible)
            d.click()