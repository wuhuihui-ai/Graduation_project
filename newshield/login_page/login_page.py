from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from newshield.base_page.base_page import BasePage
from newshield.utils.utils import Utils


class LoginPage(BasePage):
    def login(self, phone_num, pwd):
        self.find_and_clear(MobileBy.ID, "com.csizg.security:id/et_user_phone")
        self.find_and_send_keys(MobileBy.ID, "com.csizg.security:id/et_user_phone", phone_num)
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/et_password")
        self.find_and_send_keys(MobileBy.ID, "com.csizg.security:id/et_password", pwd)
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/btn_login")
        mixin = self.finds(MobileBy.ID, "com.csizg.security:id/rb_main_mixin")
        return len(mixin)
