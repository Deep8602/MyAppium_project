import base64
import os

from src.Appium_driver.Appium_driver import Appium_driver
from src.components.front.UI_elements.PointsPropositionBlock import PointsPropositionBlock
from test_suits.BaseUITest import BaseUITest


class Test_test(Appium_driver):

    def test_recording(self):
        driver = Appium_driver.get_driver()

        print(12345)
        video_data = driver.stop_recording_screen()
        print(123)
        filepath = os.path.join("D:/Automation/Mobile_appium_android/Screenshots", "video2.mp4")
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_data))

