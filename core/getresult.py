#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import allure
from requests import Response
from common.GlobalVariable import var
from common.RegExp import regexps


def get_result(r: Response, case_info):
    """获取值"""
    if case_info['extractresult']:
        for i in case_info['extractresult']:
            setattr(var, i, regexps(i, r.text))
            pytest.assume(hasattr(var, i))
    with allure.step("提取返回结果中的值"):
        for i in case_info['extractresult']:
            allure.attach(name="提取%s" % i, body=getattr(var, i))
