#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import pytest
from common.request import *
from common.readyaml import route
from tools.log import logger


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
        r = get(route['天气'], params=payload)
        logger.info(r)

    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_002(self, cityname):
        """获取城市当天的天气"""
        payload = {
            'appid': '86854339',
            'appsecret': '1IwzSyP1',
            'version': 'v6',
            'city': cityname
        }
        r = get(route['天气'], params=payload)
        logger.info(r)


if __name__ == "__main__":
    pytest.main(['Test/test_api.py'])
