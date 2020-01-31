from src.Appium_driver.Appium_driver import Appium_driver


class BaseUITest:

    def setup(self):
        self.driver = Appium_driver.get_driver()

    def teardown(self):
        print("Yes!")
        Appium_driver.close_driver()




