import re
import typing as t
import pytest
import allure
from requests import Response
from common.cache import cache
from common.regular import re, get_var, findalls
from utils.logger import logger


def get_result(r: Response, extract: t.List) -> None:
    """获取值"""
    for key in extract:
        value = get_var(key, r.text)
        logger.info("正则提取结果值：{}={}".format(key, value))
        cache.set(key, value)
        pytest.assume(key in cache)
    with allure.step("提取返回结果中的值"):
        for key in extract:
            allure.attach(name="提取%s" % key, body=cache.get(key))


def check_results(r: Response, validate: t.Dict) -> None:
    """检查运行结果"""
    expectcode = validate.get('expectcode')
    resultcheck = validate.get('resultcheck')
    regularcheck = validate.get('regularcheck')
    if expectcode:
        with allure.step("校验返回响应码"):
            allure.attach(name='预期响应码', body=str(expectcode))
            allure.attach(name='实际响应码', body=str(r.status_code))
    pytest.assume(expectcode == r.status_code)
    if resultcheck:
        with allure.step("校验响应预期值"):
            allure.attach(name='预期值', body=str(resultcheck))
            allure.attach(name='实际值', body=r.text)
        pytest.assume(resultcheck in r.text)
    if regularcheck:
        with allure.step("正则校验返回结果"):
            allure.attach(name='预期正则', body=regularcheck)
            allure.attach(name='响应值', body=str(
                re.findall(regularcheck, r.text)))
        pytest.assume(re.findall(regularcheck, r.text))