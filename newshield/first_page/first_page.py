from appium.webdriver.common.mobileby import MobileBy

from newshield.base_page.base_page import BasePage
from newshield.contact.contact_list_page import ContactListPage


class FirstPage(BasePage):
    def goto_contact(self):
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/rb_main_friends")
        return ContactListPage(self.driver)
