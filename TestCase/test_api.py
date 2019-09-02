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

sys.path.append('.')
import json
import pytest
from common.request import *
from common.readyaml import Route
from utils.dbconnect import SQLite

route = Route()


class TestShiJingLi:

    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_001(self, cityname):
        """登录接口"""
        print(cityname)
        payload = {
            'appid': '86854339',
            'appsecret': '1IwzSyP1',
            'version': 'v1',
            'city': cityname
        }
        log.info(conf.host)
        log.info(route)
        r = get(url=conf.host + route.天气, params=payload)
        log.info(json.dumps(r['json'],sort_keys=True,indent=4,ensure_ascii=False))


if __name__ == "__main__":
    pytest.main(['-v', 'TestCase/test_api.py'])
