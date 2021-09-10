#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import pytest
import allure
from requests import Response
from common.cache import cache
from common.regular import regexps
from utils.logger import Logger


def get_result(r: Response, extract):
    """获取值"""
    for i in extract:
        value = regexps(i, r.text)
        log.info("正则提取结果值：{}={}".format(i, value))
        is_vars[i] = value
        pytest.assume(i in is_vars)
    with allure.step("提取返回结果中的值"):
        for i in extract:
            allure.attach(name="提取%s" % i, body=is_vars[i])


def check_results(r: Response, case_info):
    """检查运行结果"""
    with allure.step("校验返回响应码"):
        allure.attach(name='预期响应码', body=str(case_info['expectcode']))
        allure.attach(name='实际响应码', body=str(r.status_code))
    pytest.assume(case_info['expectcode'] == r.status_code)
    if case_info['resultcheck']:
        with allure.step("校验响应预期值"):
            allure.attach(name='预期值', body=str(case_info['resultcheck']))
            allure.attach(name='实际值', body=r.text)
        pytest.assume(case_info['resultcheck'] in r.text)
    if case_info['regularcheck']:
        with allure.step("正则校验返回结果"):
            allure.attach(name='预期正则', body=case_info['regularcheck'])
            allure.attach(name='响应值', body=str(re.findall(case_info['regularcheck'], r.text)))
        pytest.assume(re.findall(case_info['regularcheck'], r.text))
