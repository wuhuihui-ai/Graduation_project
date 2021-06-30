from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from newshield.base_page.base_page import BasePage
from newshield.contact.add_friend_page import AddFriendPage
from newshield.contact.new_friend_page import NewFriendPage
from newshield.contact.set_friend import SetFriend


class ContactListPage(BasePage):
    # 点击右上角+，点击添加好友
    def add_contact_button(self):
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/iv_title_menu")
        self.find_and_click(MobileBy.XPATH, "//*[@text= '添加好友']")
        return AddFriendPage(self.driver)

    # 点击新的好友，进入新的好友列表
    def new_friend(self):
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/iv_civ")
        return NewFriendPage(self.driver)

    # 点击我的好友，进入好友列表
    def my_friend(self, text):
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/iv_my_friends")
        ele = self.scroll_search(text)
        return ele

    # 找到某个好友
    def search_friend(self, text):
        action = TouchAction(self.driver)
        action.long_press(self.my_friend(text)).release().perform()
        return SetFriend(self.driver)

