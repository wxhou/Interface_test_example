#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import allure
from tools.logger import log
from requests import Response
from common.variable import is_vars
from common.RegExp import regexps


def get_result(r: Response, extractresult):
    """获取值"""
    for i in extractresult:
        value = regexps(i, r.text)
        log.info("正则提取结果值:{}={}：".format(i, value))
        setattr(is_vars, i, value)
        pytest.assume(hasattr(is_vars, i))
    with allure.step("提取返回结果中的值"):
        for i in extractresult:
            allure.attach(name="提取%s" % i, body=getattr(is_vars, i))
