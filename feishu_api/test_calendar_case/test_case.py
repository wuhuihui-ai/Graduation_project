"""
测试类，存放测试case
"""

import allure
import pytest

from feishu_api.calendar_modlue.calendar_api import CalendarApi
from feishu_api.utils.utils import Utils


@allure.feature("日历业务场景操作")
class TestCase:
    def setup(self):
        token_data = "../data/token_data.yaml"
        url_path = "../data/url_data.yaml"
        calendar_data = "../data/calendar_data.yaml"
        # 获取token需要的id和secret
        app_id = Utils.get_data(token_data)["app_id"]
        app_secret = Utils.get_data(token_data)["app_secret"]
        # 获取token的url
        token_url = Utils.get_data(url_path)["token_url"]
        self.calendar = CalendarApi(app_id, app_secret, token_url)
        # 创建日历的url
        self.create_url = Utils.get_data(url_path)["create_calendar_url"]
        # 获取日历的url
        self.get_url = Utils.get_data(url_path)["get_calendar_url"]
        # 获取日历列表的url
        self.list_url = Utils.get_data(url_path)["calendar_list_url"]
        # 更新日历的url
        self.update_url = Utils.get_data(url_path)["update_calendar_url"]
        # 搜索日历的url
        self.search_url = Utils.get_data(url_path)["search_calendar_url"]
        # 订阅日历的url
        self.ding_yue_url = Utils.get_data(url_path)["ding_yue_url"]
        # 取消订阅的url
        self.cancle_url = Utils.get_data(url_path)["cancle_ding_url"]
        # 删除日历的url
        self.delete_url = Utils.get_data(url_path)["delete_calendar_url"]
        # 创建日历的数据
        self.creat_data = Utils.get_data(calendar_data)["create_calendar"]
        # 需要更新的日历的数据
        self.update_data = Utils.get_data(calendar_data)["update_calendar"]["data"]
        # 需要查询的日历的数据
        self.search_data = Utils.get_data(calendar_data)["search_calendar"]["data"]

    @allure.story("创建日历")
    def test_create_calendar(self):
        with allure.step("创建一个日历"):
            self.calendar.create_calendar(self.create_url, self.creat_data["data1"])
        with allure.step("获取日历列表"):
            list = self.calendar.get_calendar_list(self.list_url)
        with allure.step("通过jsonpath进行断言"):
            summary_list = Utils.assert_msg(list, "$..summary")
            assert self.creat_data["data1"]["summary"] in summary_list

    @allure.story("获取单个日历信息")
    def test_get_calendar(self):
        with allure.step("先创建一个日历"):
            self.create = self.calendar.create_calendar(self.create_url, self.creat_data["data2"])
        with allure.step("1、获取创建的日历的calendar_id"
                         "2、通过calendar_id获取日历信息"):
            r = self.calendar.get_calendar(self.get_url, self.create["data"]["calendar"]["calendar_id"])
            assert r["code"] == 0
            assert r['data']['summary'] == self.creat_data["data2"]["summary"]

    @allure.story("更新日历信息")
    def test_update_calendar(self):
        with allure.step("先创建一个日历"):
            self.create1 = self.calendar.create_calendar(self.create_url, self.creat_data["data3"])
        with allure.step("1、获取创建的日历的calendar_id"
                         "2、通过calendar_id进行修改更新"):
            r = self.calendar.update_calendar(self.update_url, self.update_data,
                                          self.create1["data"]["calendar"]["calendar_id"])
        with allure.step("获取日历列表"):
            list = self.calendar.get_calendar_list(self.list_url)
        with allure.step("通过jsonpath进行断言"):
            summary_list = Utils.assert_msg(list, "$..summary")
            assert r['data']['summary'] in summary_list

    @allure.story("搜索日历")
    def test_search_calendar(self):
        with allure.step("1、通过搜索关键字进行查询"
                         "2、并把查询的结果放在列表中"):
            r = self.calendar.search_calendar(self.search_url, self.search_data)
            list = r['data']['items']
            assert len(list) > 0

    @allure.story("订阅日历")
    def test_ding_yue(self):
        with allure.step("先创建一个日历"):
            self.create2 = self.calendar.create_calendar(self.create_url, self.creat_data["data4"])
        with allure.step("1、获取创建的日历的calendar_id"
                         "2、通过calendar_id进行订阅"):
            r = self.calendar.ding_yue(self.ding_yue_url, self.create2["data"]["calendar"]["calendar_id"])
            assert r['code'] == 0

    @allure.story("取消订阅日历")
    def test_cancle_ding_yue(self):
        with allure.step("先创建一个日历"):
            self.create3 = self.calendar.create_calendar(self.create_url, self.creat_data["data5"])
        with allure.step("1、获取创建的日历的calendar_id"
                         "2、通过calendar_id进行取消订阅"):
            r = self.calendar.cancle_ding_yue(self.cancle_url, self.create3["data"]["calendar"]["calendar_id"])
            print(r)
            assert r['code'] == 0

    @allure.story("删除日历")
    def test_detele_calendar(self):
        with allure.step("先创建一个日历"):
            self.create4 = self.calendar.create_calendar(self.create_url, self.creat_data["data6"])
        with allure.step("1、获取创建的日历的calendar_id"
                         "2、通过calendar_id删除目标日历"):
            self.calendar.delete_calendar(self.delete_url, self.create4["data"]["calendar"]["calendar_id"])
        with allure.step("获取日历列表"):
            list = self.calendar.get_calendar_list(self.list_url)
        with allure.step("通过jsonpath进行断言"):
            summary_list = Utils.assert_msg(list, "$..summary")
            assert self.creat_data["data6"]["summary"] not in summary_list