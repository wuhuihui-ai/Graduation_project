import logging
import time

import yaml
from jsonpath import jsonpath


class Utils:
    @classmethod
    def assert_msg(cls, obj, json_expr):
        """
        封装jsonpath断言
        :param obj: 要断言的json格式的响应内容
        :param json_expr: jsonpath的表达式
        :return: 提取响应内容中置顶的某一项，并存放在列表中
        """
        return jsonpath(obj, json_expr)

    @classmethod
    def get_data(cls, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def log(cls):
        """
        封装log方法
        :return:
        """
        logger = logging.getLogger("logger")
        logger.setLevel("INFO")
        if not logger.handlers:
            handler = logging.FileHandler(filename=f"../logs/file_log.log", encoding="utf-8")
            formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s", datefmt="%Y-%m-%d_%H_%M_%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

