#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import yaml
from config import conf
from common.readconfig import ini


class ReadRoute:
    """获取API路径"""

    def __init__(self):
        with open(conf.ROUTE_PATH, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取api_url"""
        return ini.host + self.data[item]


route = ReadRoute()

__all__ = ['route']

if __name__ == '__main__':
    print(route['天气'])
