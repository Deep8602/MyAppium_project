from appium import webdriver



class Appium_driver():

    _instance = None

    desired_caps_emul = {}
    desired_caps_emul['deviceName'] = 'emulator-5554'
    desired_caps_emul['platformName'] = 'Android'
    desired_caps_emul['platformVersion'] = '8.0.0'
    desired_caps_emul['appPackage'] = 'ua.silpo.android'
    desired_caps_emul['appActivity'] = 'ua.silpo2.android.ui.activity.MainActivity'
    desired_caps_emul['unicodeKeyboard'] = True
    desired_caps_emul['noReset'] = True


    desired_caps_tel = {}
    desired_caps_tel['deviceName'] = 'PAG4C17916001004'
    desired_caps_tel['platformName'] = 'Android'
    desired_caps_tel['platformVersion'] = '8.0.0'
    desired_caps_tel['appPackage'] = 'ua.silpo.android'
    desired_caps_tel['appActivity'] = 'ua.silpo2.android.ui.activity.MainActivity'
    desired_caps_emul['unicodeKeyboard'] = True
    desired_caps_tel['noReset'] = True

    @classmethod
    def get_driver(cls):
        if not cls._instance:
            cls._instance = Appium_driver()
            cls._driver = cls._instance._driver
        return cls._driver

    def __init__(self):
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps_tel)
        # self._driver.find_element_by_id()




    @classmethod
    def close_driver(cls):
        cls._driver.quit()
        cls._instance = None


    # def recording(self):
    #     self.get_driver()
    #     self._driver.start_recording_screen()
    #     print(12345)
    #     self._driver.stop_recording_screen()

    # def get_webdriver(cls):
    #     if not cls._instance:
    #         cls._instance = DriverWrapper()
    #         cls._driver = cls._instance._driver
    #     return cls._driver
    # def __init__(self):
    #     webdrivers_path = os.path.dirname(WebDrivers.__file__)
    #     browser_name = settings.browser_name
    #
    #     if browser_name == 'Chrome':
    #         options = webdriver.ChromeOptions()
    #
    #         drivers_path = os.path.join(webdrivers_path, "chromedriver.exe")
    #         self._driver = webdriver.Chrome(executable_path=drivers_path, chrome_options=options)
    #         self._driver.set_page_load_timeout(60)




      #
        # if device_name == "emulator":
        #     return webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps_emul)
        # elif device_name == "my_tel":
        #     return webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps_tel)








