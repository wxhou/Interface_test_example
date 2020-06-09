#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import os
import logging
from config import conf
from datetime import datetime


class Logger:
    def __init__(self, name):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
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
        return '%(levelname)s\t%(asctime)s %(filename)s:%(lineno)d %(name)s %(message)s'

    @property
    def log_path(self):
        month = datetime.now().strftime("%Y%m")
        return os.path.join(conf.LOG_PATH, '{}.log'.format(month))


logger = Logger('demo').logger

__all__ = ['logger']
if __name__ == '__main__':
    logger.info("你好")
