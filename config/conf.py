#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from utils.times import datetime_strftime


class ConfigManger(object):
    # 项目目录
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # 数据文件
    DATA_DIR = os.path.join(BASE_DIR, 'apiData')

    # 日志目录
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    @property
    def log_file(self):
        """日志文件"""
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)
        return os.path.join(self.LOG_DIR, '{}.log'.format(datetime_strftime()))

cm = ConfigManger()
if __name__ == "__main__":
    print(cm.BASE_DIR)
