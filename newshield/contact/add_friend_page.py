from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from newshield.base_page.base_page import BasePage


class AddFriendPage(BasePage):
    """
        1、进入添加好友页
        2、点击搜索联系人
        3、点击搜索框，输入手机号，点击添加
        4、页面跳转到新的好友页，查看好友验证是否发送成功
    """

    def search_number(self, phone_number):
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/add_friend_from_phone")
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/et_user_phone")
        self.find_and_send_keys(MobileBy.ID, "com.csizg.security:id/et_user_phone", phone_number)
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/add_number_search")
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加']")
        send_button = (MobileBy.ID, "com.csizg.security:id/add_number_contacts_add")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(send_button))
        self.find_and_click(*send_button)
        new = self.finds(MobileBy.ID, "com.csizg.security:id/iv_civ")
        return new
