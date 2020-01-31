# -- coding: utf-8 --
import base64
import os
import time

import pytest

from src.components.front.UI_elements.BaseFunctionality import BaseFunctionality
from src.components.front.UI_elements.FirstPage import FirstPage
from src.components.front.UI_elements.PointsPropositionBlock import PointsPropositionBlock
from test_suits.BaseUITest import BaseUITest


class Test_FirstPage(BaseUITest):

    def test_scroll_to_buttom(self):
        """Перевірка можливості скролу до нижньої частини сторінки і перевірка наявності віджиту "Кераміка від Марко Черветті"
        (при зміні акції змінити локатор!)
        (використовуться xpath локатор може бути змінений!)"""
        first_page = FirstPage()
        first_page.swipe_down_to_element(first_page.marko_ceramics_loc)# елемент може бути змінений (змінеться xpath або закіньчиться сама акція)
        assert first_page.get_text_from_element(first_page.marko_ceramics_loc)== 'Кераміка від Марко Черветті', "text element not 'Кераміка від Марко Черветті' "
        first_page.get_screenshot()

    def test_scroll_horizontally(self):
        """Перевірка можливості горизонтального скролу по колонці "бонуси" перевірка наявності віджиту "Наступний бонус"
            (використовуться xpath локатор може бути змінений!)"""
        first_page = FirstPage()
        first_page.swipe_horizontally(first_page.next_bonus_loc)
        assert first_page.get_text_from_element(first_page.next_bonus_loc) =="Наступний бонус", "text element not 'Наступний бонус' "


    def test_write_in_email_field(self):
        """Перевірка можливості друку в полі email, та роботу валідації пошти"
        """
        first_page = FirstPage()
        first_page.tap_to_menu_button()
        first_page.click(first_page.personal_data_loc)\
            .click(first_page.edit_personal_data_loc)
        first_page.swipe_down_to_element(first_page.email_loc)
        first_page.click(first_page.email_loc)\
            .send_keys(first_page.email_loc, 'hello_world')
        assert first_page.get_text_from_element(first_page.email_hint_loc) == 'Електронна адреса (Некоректна адреса)', "hint 'Invalid addresses' not displayed "
        time.sleep(5)


    def test_go_to_action_page(self):
        """Перевірка можливості переходу на закладку "Акції" та перевірка наявності кнопки "Обрати магазин"
            (використовуються координати кнопки)"""
        first_page = FirstPage()
        first_page.tap_to_action_button()
        assert first_page.is_element_visible(first_page.choose_store_loc), "we don\'t go to action page, or widget choose store don\'t visible"

    def test_go_to_history(self):
        """Перевірка можливості переходу на закладку "Історія" та перевірка наявності віджету "кількість балів"
                   (використовуються координати кнопки)"""
        first_page = FirstPage()
        first_page.tap_to_history_button()
        assert first_page.is_element_visible(first_page.header_points_loc), "we don\'t go to history page, or widget points don\'t visible"

    def test_go_to_menu(self):
        """Перевірка можливості переходу на закладку "Меню" та перевірка наявності віджету "Ім"я"
                          (використовуються координати кнопки)"""
        first_page = FirstPage()
        first_page.tap_to_menu_button()
        assert first_page.is_element_visible(first_page.header_name_loc), "we don\'t go to menu page, or widget name don\'t visible"





