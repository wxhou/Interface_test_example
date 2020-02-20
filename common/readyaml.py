#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : readyaml.py
@Time : 2020-02-17 16:18:30
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import yaml
import settings
from common.readconfig import ini


class ReadRoute:
    """路径"""
    def __init__(self):
        with open(settings.ROUTE_PATH, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        item_data = self.data.get(item)
        if item_data: return ini.host + item_data
        raise ValueError("{} 路径不存在".format(item))


route = ReadRoute()

if __name__ == '__main__':
    print(route.天气)
