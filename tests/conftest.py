#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pytest
from core.request import req
from common.ApiData import testinfo
from core.checkresult import check_results


@pytest.fixture(scope='session')
def is_login(request):
    """登录"""
    r = req(testinfo.login_info('method'), testinfo.login_info('route'),
            testinfo.login_info('extractresult'), **testinfo.login_info('RequestData'))
    result = json.loads(r.text)
    check_results(r, testinfo.stand_info('登录'))
    if 'token' in result:
        req.headers['Authorization'] = "JWT " + result['token']

    def fn():
        req.r.close()

    request.addfinalizer(fn)


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


if __name__ == '__main__':
    pass
