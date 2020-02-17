#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : logger.py
@Time : 2020-02-17 16:17:44
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import os
import logging
import settings
from datetime import datetime



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
        month = datetime.now().strftime("%Y%m")
        return os.path.join(settings.LOG_PATH, '{}.log'.format(month))


log = Log().logger

if __name__ == '__main__':
    log.info("你好")
