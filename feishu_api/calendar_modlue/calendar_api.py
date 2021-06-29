import requests

from feishu_api.base_modlue.get_token import GetToken


class CalendarApi(GetToken):
    # 创建日历
    def create_calendar(self, url, data):
        req = {
            "method": "POST",
            "url": url,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": data
        }
        r = self.get_request(req)
        return r.json()

    # 获取日历
    def get_calendar(self, url, calendar_id):
        url_pa = f"{url}{calendar_id}"
        req = {
            "method": "GET",
            "url": url_pa,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
        }
        r = self.get_request(req)
        return r.json()

    # 获取日历列表
    def get_calendar_list(self, url):
        req = {
            "method": "GET",
            "url": url,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
        }
        r = self.get_request(req)
        return r.json()

    # 更新日历
    def update_calendar(self, url, data, calendar_id):
        url_pa = f"{url}{calendar_id}"
        req = {
            "method": "PATCH",
            "url": url_pa,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": data
        }
        r = self.get_request(req)
        return r.json()

    # 搜索日历
    def search_calendar(self, url, data):
        req = {
            "method": "POST",
            "url": url,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": data
        }
        r = self.get_request(req)
        return r.json()

    # 订阅日历
    def ding_yue(self, url, calendar_id):
        url_pa = f"{url}{calendar_id}/subscribe"
        req = {
            "method": "POST",
            "url": url_pa,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
        }
        r = self.get_request(req)
        return r.json()

    # 取消订阅日历
    def cancle_ding_yue(self, url, calendar_id):
        url_pa = f"{url}{calendar_id}/unsubscribe"
        req = {
            "method": "POST",
            "url": url_pa,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
        }
        r = self.get_request(req)
        return r.json()

    # 删除日历
    def delete_calendar(self, url, calendar_id):
        url_pa = f"{url}{calendar_id}"
        req = {
            "method": "DELETE",
            "url": url_pa,
            "headers": {
                "Authorization": f"Bearer {self.app_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
        }
        r = self.get_request(req)
        return r.json()
