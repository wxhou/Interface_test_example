#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   request.py
@Time    :   2019/09/02 10:31:45
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
import os

sys.path.append('.')
import logging
from datetime import datetime

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Log:
    def __init__(self):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.logger = logging.getLogger()
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
        return '%(levelname)s\t%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(name)s %(message)s'

    @property
    def log_path(self):
        month = datetime.now().strftime("%Y%mweek%W")
        return os.path.join(root_dir, 'logs', '{}.log'.format(month))


if __name__ == '__main__':
    log = Log().logger
    print(log.info("你好"))
