import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

from src.Appium_driver.Appium_driver import Appium_driver



class BaseFunctionality:


    wait_element_time = 20

    def __init__(self):
        self.driver = Appium_driver.get_driver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)


    def click(self, element_locator:tuple):
        """
        Searches the element on the page (in dom), from given locator and click on it;
        :param element_locator: id, class_name and other options to search the web element
        :return: self
        """
        element = self.wait.until(EC.presence_of_element_located(element_locator), 'element not found')
        element.click()
        return self


    def is_element_visible(self, locator: tuple):
        """ Looking for element with given locator and check if this element is visible
        :param: locator
        :return: Returns 'True' if the web-element is visible, otherwise returns 'False'"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_text_from_element(self, locator: tuple):
        """
        	:return: text of selected еlement
        	:param: locator
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        print(element.get_attribute("text"))
        return element.get_attribute("text")

    def swipe_to_up(self, range_num: int):
        """ Makes swipe to up given nomber of times
            :param: nomber of times to make swipe
        """
        tuch = TouchAction(self.driver)
        for _ in range(range_num):
            tuch.press(x=912, y=387).move_to(x=38, y=798).release().perform()

    def swipe_to_down(self, range_num: int):
        """ Makes swipe to down given nomber of times
            :param: nomber of times to make swipe
        """
        tuch = TouchAction(self.driver)
        for _ in range(range_num):
            tuch.press(x=689, y=1358).move_to(x=14, y=-825).release().perform()

    def get_screenshot(self):
        """ Makes screenshot and save in a specific directory
            :param: number of times to make swipe
        """

        scr_name = time.strftime("%Y_%m_%d_%H.%M.%S")
        self.driver.save_screenshot("D:/Automation/Mobile_appium_android/Screenshots/" + scr_name + ".png")







    # def start_recording_video(self):
    #     path = "D:/Automation/Mobile_appium_android/Screenshots/video1.png"
    #     self.driver.start_recording_screen()
    #
    #
    # def stop_recording_video(self):
    #     self.driver.stop_recording_screen()
    #
    #     filepath = os.path.join("D:/Automation/Mobile_appium_android/Screenshots", "video2.mp4")
    #     with open(filepath, "wb") as vd:
    #         vd.write(base64.b64decode(video_data))
    #






    # def beck(self):
    #     tuch = TouchAction(self.driver)
    #     tuch.press(x=66, y=165).release().perform()



