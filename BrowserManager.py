import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Browser:

    CHROME = 1
    FF = 2
    PHANTOM = 3
    IE = 4
    OPERA = 5

    __DRIVER_MAP = {}
    @staticmethod
    def create_new_driver(driver_id):

        thread_object = threading.currentThread()

        def get_driver():
            if Browser.PHANTOM == driver_id:
                driver = webdriver.PhantomJS()

            elif Browser.CHROME == driver_id:
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

            elif Browser.FF == driver_id:
                driver = webdriver.Firefox()

            elif Browser.OPERA == driver_id:
                driver = webdriver.Opera()

            elif Browser.IE == driver_id:
                driver = webdriver.Ie()
            else:
                raise Exception("There is no support for driver_id: {}".format(driver_id))
            return driver

        Browser.__map(thread_object, get_driver())
        return Browser.get_driver()

    @staticmethod
    def get_driver():
        # print "Getting  driver for thread: {}".format(threading.currentThread())
        return Browser.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def __map(thread, driver):

        Browser.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def get_driver_map():
        return Browser.__DRIVER_MAP

    @staticmethod
    def shutdown():

        Browser.get_driver().quit()
