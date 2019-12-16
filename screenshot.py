# Author: Laurel Miller
from os import listdir
import time


class Screenshot(object):
    def __init__(self, driver, screen_shot_name):
        self.driver = driver
        self.screen_shot_name = screen_shot_name
        self.time_stamp = time.strftime("%Y-%m-%d_%H-%M")

    def take_screenshot(self):
        self.driver.save_screenshot(
            "../screenshots/" + self.screen_shot_name + ' ' + self.time_stamp + ".png"
        )
        time.sleep(5)

    def open_screenshot(self):
        image_source = 'C:\PycharmProjects\src\AlscoMaster\Challenges\screenshots.py'
        try:
            for file in listdir(image_source):
                if file.startswith(self.screen_shot_name):
                    file_name = 'file://' + image_source + file
                    self.driver.get(file_name)
                    time.sleep(5)
        finally:
            pass


