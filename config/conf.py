#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 接口路径数据
ROUTE_PATH = os.path.join(BASE_DIR, 'Data', 'api_url.yaml')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告文件
REPORT_PATH = os.path.join(BASE_DIR, 'report.html')

if __name__ == "__main__":
    print(BASE_DIR)