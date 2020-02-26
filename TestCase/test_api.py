#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : test_api.py
@Time : 2020-02-17 16:18:48
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import pytest
from common.request import request, logger
from common.readyaml import route


class TestWeather:
    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_001(self, cityname):
        """获取城市七天天气"""
        payload = {
            'appid': '86854339',
            'appsecret': '1IwzSyP1',
            'version': 'v1',
            'city': cityname
        }
        r = request.get(route('天气'), params=payload)
        logger.info(r.json())

    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_002(self, cityname):
        """获取城市当天的天气"""
        payload = {
            'appid': '86854339',
            'appsecret': '1IwzSyP1',
            'version': 'v6',
            'city': cityname
        }
        r = request.get(route('天气'), params=payload)
        logger.info(r.json())


if __name__ == "__main__":
    pytest.main(['TestCase/test_api.py'])
