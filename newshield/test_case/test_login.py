import allure
import pytest

from newshield.app_launch.app_launch import AppLaunch
from newshield.utils.utils import Utils


@allure.feature("登录模块业务场景")
@pytest.mark.run(order=1)
class TestLogin:
    login_data = "../data/login_data.yaml"

    def setup(self):
        self.launch = AppLaunch()

    def teardown(self):
        self.launch.app_close()

    @pytest.mark.run(order=1)
    @allure.story("测试登录模块")
    @pytest.mark.parametrize("phone_num, pwd, udid1, version1, expect", [
        Utils.yaml_data(login_data)["data1"],
        Utils.yaml_data(login_data)["data2"],
        Utils.yaml_data(login_data)["data3"],
        Utils.yaml_data(login_data)["data4"],
    ])
    def test_login(self, phone_num, pwd, udid1, version1, expect):
        with allure.step("1、进入登录页，输入账号和密码，点击登录"):
            result = self.launch.app_launch(udid1, version1).goto_login().login(phone_num, pwd)
            assert result == expect
