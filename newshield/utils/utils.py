import logging

import yaml


class Utils:
    @classmethod
    def yaml_data(cls, yamlpath):
        with open(yamlpath, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def log(cls):
        # 创建日志器
        logger = logging.getLogger("logger")
        # 设置日志级别
        logger.setLevel("INFO")
        if not logger.handlers:
            # 创建文件处理器，存放日志到对应文件夹内
            fh = logging.FileHandler("../logs/TEST.log", encoding="utf-8")
            # 创建格式器
            formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s", datefmt="%Y-%m-%d %H%M%S")
            # 设置日志文件内可放入的日志级别
            fh.setLevel("INFO")
            # 给处理器设置设置格式
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger

