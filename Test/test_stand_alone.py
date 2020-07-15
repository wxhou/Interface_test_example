#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import allure
from core.request import req
from common.ApiData import testinfo
from core.checkresult import check_results


@allure.feature("单个API测试")
class TestStandAlone:

    @pytest.mark.parametrize('case', testinfo.stand_alone.values(), ids=testinfo.stand_alone.keys())
    def test_stand_alone_interface(self, case):
        r = req(case['method'], case['route'], **case['RequestData'])
        check_results(r, case)


if __name__ == "__main__":
    pytest.main(['test_business.py'])
