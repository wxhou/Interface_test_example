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
    r = req(testinfo.login_info('method'), testinfo.login_info('route'), **testinfo.login_info('RequestData'))
    result = json.loads(r.text)
    req.headers['Authorization'] = "JWT " + result['token']
    check_results(r, testinfo.stand_info('登录'))

    def fn():
        req.close_session()

    request.addfinalizer(fn)
    return result['token']


if __name__ == '__main__':
    pass