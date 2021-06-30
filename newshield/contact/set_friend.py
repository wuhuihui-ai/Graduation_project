from appium.webdriver.common.mobileby import MobileBy

from newshield.base_page.base_page import BasePage


class SetFriend(BasePage):
    # 设置备注
    def set_remark(self, remark):
        from newshield.contact.contact_list_page import ContactListPage
        self.find_and_click(MobileBy.XPATH, "//*[@text= '设置备注']")
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/et_remark")
        self.find_and_clear(MobileBy.ID, "com.csizg.security:id/et_remark")
        self.find_and_send_keys(MobileBy.ID, "com.csizg.security:id/et_remark", remark)
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/ok")
        return ContactListPage(self.driver)

    # 删除好友
    def delete_friend(self):
        from newshield.contact.contact_list_page import ContactListPage
        self.find_and_click(MobileBy.XPATH, "//*[@text= '删除好友']")
        self.find_and_click(MobileBy.ID, "com.csizg.security:id/confim_update")
        return ContactListPage(self.driver)
