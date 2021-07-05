import requests

from feishu_api.utils.utils import Utils


class BaseMethod:
    def get_request(self, req):
        """
        封装请求方法
        :param req:需要传入关键字参数
        :return:接口响应信息
        **req为解字典
        """
        try:
            Utils.log().info("--------request data-------")
            Utils.log().info(req)
            r = requests.request(**req)
            Utils.log().info("--------response data-------")
            Utils.log().info(r.json())
            return r
        except Exception as e:
            Utils.log().exception(e)



