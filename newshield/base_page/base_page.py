import logging
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from newshield.utils.utils import Utils


class BasePage:
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def find(self, by, locator):
        Utils.log().info("-------------find----------------")
        Utils.log().info(by)
        Utils.log().info(locator)
        try:
            ele = self.driver.find_element(by, locator)
            return ele
        except Exception as e:
            # self.screenshot()
            Utils.log().exception(e)

    def find_and_click(self, by, locator):
        Utils.log().info("------------find_and_click-------------")
        try:
            ele = self.find(by, locator).click()
            return ele
        except Exception as e:
            # self.screenshot()
            Utils.log().exception(e)

    def find_and_send_keys(self, by, locator, key):
        Utils.log().info("-----------find_and_send_keys------------")
        try:
            ele = self.find(by, locator).send_keys(key)
            return ele
        except Exception as e:
            # self.screenshot()
            Utils.log().exception(e)

    def find_and_clear(self, by, locator):
        Utils.log().info("-----------find_and_clear------------")
        try:
            ele = self.find(by, locator).clear()
            return ele
        except Exception as e:
            # self.screenshot()
            Utils.log().exception(e)

    def finds(self, by, locator):
        Utils.log().info("-----------finds------------")
        try:
            ele = self.driver.find_elements(by, locator)
            return ele
        except Exception as e:
            # self.screenshot()
            Utils.log().exception(e)

    # 滚动查找某个元素
    def scroll_search(self, text, num=3):
        for i in range(num):
            try:
                member = (MobileBy.XPATH, f"//*[contains(@text, '{text}')]")
                WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(member))
                ele = self.find(*member)
                return ele
            except:
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 4 / 5
                end_x = width / 2
                end_y = height * 1 / 5
                duration: int = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def screenshot(self):
        timestr = time.strftime("%Y-%m-%d_%H_%M_%S")  # 定义截图名称即时间戳，字符串类型
        self.driver.get_screenshot_as_file(
            "../logs/screenshot_picture/picture" + timestr + ".png")

    def wait(self, timeout=10, poll_frequency=0.5, method=None):
        WebDriverWait(self.driver, timeout, poll_frequency).until(method)
