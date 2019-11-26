#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import json
import pytest
from common.request import *
from common.readyaml import route, payload
from utils.dbconnect import SQLite



class TestWeather:

    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_001(self, cityname):
        """获取城市七天天气"""
        payload.test_001['city'] = cityname
        r = get(url=conf.host + route.天气, params=payload.test_001)
        log.info(json.dumps(r.json(), sort_keys=True, indent=4, ensure_ascii=False))

    @pytest.mark.parametrize('cityname', ['西安', '宝鸡'])
    def test_002(self, cityname):
        """获取城市当天的天气"""
        payload.test_002['city'] = cityname
        r = get(url=conf.host + route.天气, params=payload.test_002)
        log.info(json.dumps(r.json(), sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    pytest.main(['-v', 'TestCase/test_api.py'])
