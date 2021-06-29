import requests

from feishu_api.base_modlue.base_method import BaseMethod


class GetToken(BaseMethod):
    # 构造方法，用来初始化
    def __init__(self, app_id, app_secret, url):
        self.app_token = self.get_token(app_id, app_secret, url)

    # 获取API访问凭证app_access_token
    def get_token(self, app_id, app_secret, url):
        url = url
        data = {
            "app_id": app_id,
            "app_secret": app_secret
        }
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        r = requests.request("POST", url, headers=headers, json=data)
        app_access_token = r.json()['app_access_token']
        return app_access_token
