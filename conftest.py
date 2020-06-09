#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import pytest
from py._xmlgen import html
from common.readconfig import ini


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        report.extra = extra
        report.description = str(item.function.__doc__)
        # .encode("utf-8").decode("unicode_escape")
        report.nodeid = report.nodeid


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('未捕获日志输出.', class_='empty log'))


@pytest.mark.optionalhook
def pytest_configure(config):
    """测试报告环境"""
    config._metadata.clear()
    config._metadata["项目名称"] = "接口自动化测试演示"
    config._metadata['接口地址'] = ini.host
    config._metadata['所属部门'] = '测试部'
    config._metadata['测试人员'] = '侯伟轩'


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "天气网测试报告"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    """测试报告概要"""
    prefix.extend([html.p("所属部门: 测试中心")])
    prefix.extend([html.p("测试人员: 侯伟轩")])
