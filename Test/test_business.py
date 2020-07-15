#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from core.request import req
from common.ApiData import testinfo
from core.checkresult import check_results


@allure.feature("业务流程API测试")
class TestBusiness:
    @pytest.mark.parametrize('case', testinfo.business.values(), ids=testinfo.business.keys())
    def test_business_interface(self, is_login, case):
        r = req(case['method'], case['route'], **case['RequestData'])
        check_results(r, case)


if __name__ == "__main__":
    pytest.main(['test_business.py'])
