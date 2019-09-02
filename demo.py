#!/usr/bin/env python3
#coding=utf-8
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

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_path = os.path.join(root_dir, 'logs')
if os.path.exists(log_path):
    os.mkdir(log_path)