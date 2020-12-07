#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
from config.conf import cm


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.DEBUG)

            # 在控制台输出
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义hanler的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给log添加handles
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(asctime)s %(levelname)s %(name)s-line:%(lineno)d %(message)s'


if __name__ == '__main__':
    log = Logger(__name__).logger
    log.info("你好")
