#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import allure
from requests import Response
from common.variable import is_vars
from common.RegExp import regexps
from utils.logger import Logger

log = Logger(__name__).logger


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
