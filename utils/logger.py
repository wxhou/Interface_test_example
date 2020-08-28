#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
from config import conf
from datetime import datetime


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
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
        return '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s'

    @property
    def log_path(self):
        if not os.path.exists(conf.LOG_DIR):
            os.makedirs(conf.LOG_DIR)
        month = datetime.now().strftime("%Y%m")
        return os.path.join(conf.LOG_DIR, '{}.log'.format(month))


log = Logger('root').logger
if __name__ == '__main__':
    log.info("你好")
