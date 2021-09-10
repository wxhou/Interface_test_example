#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from utils.times import datetime_strftime

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 数据文件
DATA_DIR = os.path.join(BASE_DIR, 'apiData')

# 日志文件
LOGGER_DIR = os.path.join(BASE_DIR, 'logs')
