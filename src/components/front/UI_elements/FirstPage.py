import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.components.front.UI_elements.BaseFunctionality import BaseFunctionality


class FirstPage(BaseFunctionality):

    marko_ceramics_loc = (By.XPATH, "//android.widget.RelativeLayout/android.widget.TextView[@text = 'Кераміка від Марко Черветті']")
    choose_store_loc = (By.ID, 'ua.silpo.android:id/tv_filial_title')
    header_points_loc = (By.ID, 'tv_header_points_amount')
    header_name_loc = (By.ID, 'item_title_header')
    personal_prop_discription_loc = (By.ID, 'ua.silpo.android:id/text_description')

    next_bonus_loc = (By.XPATH, "//android.view.ViewGroup[2]/android.widget.TextView[1]")

    personal_data_loc = (By.ID, 'text_personal_title')
    edit_personal_data_loc = (By.ID, 'action_edit_info')
    first_name_field_loc = (By.ID,'edit_first_name')
    email_loc = (By.ID, 'edit_email')
    email_hint_loc = (By.ID, 'text_email')

    def swipe_down_to_element(self, element_loc):
        tuch = TouchAction(self.driver)
        while not self.is_element_visible(element_loc):
            tuch.press(x=689, y=1358).move_to(x=14, y=-825).release().perform()

    def swipe_horizontally(self, element_loc):
        tuch = TouchAction(self.driver)
        while not self.is_element_visible(element_loc):
            tuch.press(x=929, y=1589).move_to(x=-679, y=10).release().perform()

    def send_keys(self, element_loc,  some_text):
        self.wait.until(EC.presence_of_element_located(element_loc)).send_keys(some_text)




    def tap_to_action_button(self):
        tuch = TouchAction(self.driver)
        tuch.tap(x=325, y=1929).perform()

    def tap_to_history_button(self):
        tuch = TouchAction(self.driver)
        tuch.tap(x=745, y=1938).perform()

    def tap_to_menu_button(self):
        tuch = TouchAction(self.driver)
        tuch.tap(x=976, y=1957).perform()


