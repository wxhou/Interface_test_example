#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : settings.py
@Time : 2020-02-17 16:19:14
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import os

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config.ini')

# 接口路径数据
ROUTE_PATH = os.path.join(BASE_DIR, 'TestData', 'route.yaml')

# 请求头数据
PAYLOAD_PATH = os.path.join(BASE_DIR, 'TestData', 'payload.yaml')

# sqlite数据库
SQLITE_PATH = os.path.join(BASE_DIR, 'database', 'sqlite3.sqlite')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report.html')

if __name__ == "__main__":
    print(BASE_DIR)