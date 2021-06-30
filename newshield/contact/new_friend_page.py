from appium.webdriver.common.mobileby import MobileBy

from newshield.base_page.base_page import BasePage


class NewFriendPage(BasePage):
    def accept_add(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='吴慧']/../../../..//*["
                                            "@resource-id='com.csizg.security:id/new_friend_accept']")
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/ok")
        p = self.finds(MobileBy.XPATH, "//*[@text='吴慧']/../../../..//*["
                                       "@text='已通过']")
        return p
