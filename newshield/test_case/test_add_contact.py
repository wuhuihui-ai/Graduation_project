from time import sleep

import allure
import pytest

from newshield.app_launch.app_launch import AppLaunch
from newshield.utils.utils import Utils


@allure.feature("测试通讯录模块")
class TestContact:
    yamlpath = "../data/contact_data.yaml"

    def setup(self):
        self.launch = AppLaunch()

    # def setup(self):
    #     self.start = self.launch.app_launch().goto_first()

    def teardown(self):
        # self.launch.back()
        # self.launch.back()
        self.launch.app_close()

    @pytest.mark.run(order=2)
    @allure.story("发送方-发送好友请求")
    @pytest.mark.parametrize("udid1, version1, phone_number", Utils.yaml_data(yamlpath)["send_fri_data"])
    def test_add_contact(self, udid1, version1, phone_number):
        '''
        :param udid1: 手机的唯一标识
        :param version1: 手机的Android版本
        :param phone_number: 添加好友的手机号
        :return: 发送成功
        '''
        with allure.step("1、启动应用，进入首页"
                         "2、从首页进入通讯录，点击右上角+，点击添加好友"
                         "3、通过搜索联系人进行添加"
                         "4、输入手机号点击添加，发送好友申请，并验证请求是否发送成功"):
            result = self.launch.app_launch(udid1,
                                            version1).goto_first().goto_contact().add_contact_button().search_number(
                phone_number)
            assert len(result) > 0
            sleep(5)

    @pytest.mark.run(order=3)
    @allure.story("接收方-同意好友发送的请求")
    @pytest.mark.parametrize("udid2, version2", Utils.yaml_data(yamlpath)["accept_fri_data"])
    def test_accept(self, udid2, version2):
        '''
        :param udid2: 手机的唯一标识
        :param version2: 手机的Android版本
        :return: 同意好友申请
        '''
        with allure.step("1、启动应用，进入首页"
                         "2、点击新的好友进入"
                         "3、点击接受，验证是否同意成功"):
            result = self.launch.app_launch(udid2, version2).goto_first().goto_contact().new_friend().accept_add()
            assert len(result) > 0

    @pytest.mark.run(order=4)
    @allure.story("给好友设置备注")
    @pytest.mark.parametrize("udid1, version1, name, remark", Utils.yaml_data(yamlpath)["set_remark"])
    def test_friend_remark(self, udid1, version1, name, remark):
        '''
        :param udid1:手机的唯一标识
        :param version1:手机的Android版本
        :param name:要修改的好友的名字
        :param remark:修改后的备注
        :return:
        '''
        with allure.step("1、启动应用，进入首页"
                         "2、进入通讯录-我的好友列表"
                         "3、找到某个好友进行修改备注"):
            ele = self.launch.app_launch(udid1, version1).goto_first().goto_contact().search_friend(name).set_remark(
                remark).scroll_search(remark)
            if ele:
                print("设置备注成功")

    @pytest.mark.run(order=5)
    @allure.story("删除好友")
    @pytest.mark.parametrize("udid1, version1, remark", Utils.yaml_data(yamlpath)["delete"])
    def test_delete_friend(self, udid1, version1, remark):
        '''
        :param udid1:手机的唯一标识
        :param version1:手机的Android版本
        :param remark:要删除的好友的名字
        :return:
        '''
        with allure.step("1、启动应用，进入首页"
                         "2、进入通讯录-我的好友列表"
                         "3、找到某个好友进行删除"):
            ele = self.launch.app_launch(udid1, version1).goto_first().goto_contact().search_friend(
                remark).delete_friend().scroll_search(remark)
            if not ele:
                print("删除成功")
