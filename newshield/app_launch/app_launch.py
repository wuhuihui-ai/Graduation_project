from appium import webdriver

from newshield.base_page.base_page import BasePage
from newshield.first_page.first_page import FirstPage
from newshield.login_page.login_page import LoginPage


class AppLaunch(BasePage):
    def app_launch(self, udid, version):
        if self.driver is None:
            desire_caps = {}
            desire_caps["deviceName"] = "47S0221119008725"
            desire_caps["platformName"] = "Android"
            desire_caps["platformVersion"] = version
            desire_caps["udid"] = udid
            desire_caps["appPackage"] = "com.csizg.security"
            desire_caps["appActivity"] = ".workspace.welcome.activity.StartActivity"
            # 弹出的确认弹窗关闭后，不再弹出
            desire_caps["noReset"] = "true"
            # 停止在当前页面，不重新引用
            # desire_caps["dontStopAppOnReset"] = "true"
            # 跳过安装等操作
            desire_caps["skipDeviceInitialization"] = "true"
            desire_caps["unicodeKeyBoard"] = "true"
            desire_caps["resetKeyBoard"] = "true"
            desire_caps["autoGrantPermissions"] = True
            # desire_caps["newCommandTimeout"] = 600
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver.launch_app()
        return self

    def app_close(self):
        return self.driver.quit()

    def back(self):
        self.driver.back()

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def goto_login(self) -> LoginPage:
        return LoginPage(self.driver)

    def goto_first(self):
        return FirstPage(self.driver)
