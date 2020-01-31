from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time

from src.components.front.UI_elements.BaseFunctionality import BaseFunctionality
from selenium.webdriver.support import expected_conditions as EC

class PointsPropositionBlock(BaseFunctionality):

    points_btn_id = (By.ID, 'tv_points')
    points_chart_id = (By.ID,'chart')
    next_bonus_view_id = (By.ID,'bonus_view_base')
    next_bonus_title =(By.ID,'tv_title')
    next_bonus_date = (By.ID, 'tv_date')
    next_bonus_value = (By.ID, 'tv_value')
    next_bonus_image = (By.ID, 'iv_item_image')
    next_bonus_back = (By.ID, 'Navigate up')

    list_of_points_name = (By.ID, 'text_balance_name')
    list_of_points_image = (By.ID, 'view_image_silpo')
    list_of_points_balance = (By.ID, 'text_balance')


    def get_count_of_element_list(self, locator: tuple):
        """ Return number of elements list
              :param: locator
              :return: Returns number of elements list: int"""
        element_list = self.wait.until(EC.presence_of_all_elements_located(locator))
        return len(element_list)



