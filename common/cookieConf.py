#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from requests import Response
from common.ApiData import testinfo
from requests.cookies import RequestsCookieJar
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
from core.serialize import serialization, deserialization


def save_cookie(r: Response):
    """获取cookie"""
    cookie = serialization(dict_from_cookiejar(r.cookies))
    testinfo.self.info['test_info']['cookies'] = cookie
    return testinfo.info['test_info']['cookies']


def get_cookie(cookies):
    """获取cookie"""
    result = deserialization(cookies)
    return result


if __name__ == '__main__':
    pass
