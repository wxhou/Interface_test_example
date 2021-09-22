#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import yaml
import pytest
import pytest
import logging
from string import Template
from common.cache import cache
from common.request import HttpRequest
from common.result import get_result, check_results


logger = logging.getLogger('debug')


def pytest_collect_file(parent, path):
    if path.ext in (".yaml", ".yml") and path.basename.startswith("test"):
        logger.debug("pytest_collect_file is: {} {}".format(parent, path))
        return YamlFile.from_parent(parent, fspath=path)


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


class YamlFile(pytest.File):
    def collect(self):
        raw = yaml.safe_load(self.fspath.open(encoding='utf-8'))
        if config := raw.pop('config'):
            cache.set('baseurl', config.get('url', ''))
            cache.set('timeout', config.get('timeout', 30.0))
            cache.set('headers', config.get('headers'))
        if variable := raw.get('variable'):
            for k, v in variable.items():
                cache.set(k, v)
        logger.debug("yaml data is: {}".format(raw))
        for name, spec in raw.get('tests').items():
            yield YamlTest.from_parent(self, name=name, spec=spec)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec
        self.description = self.spec.get('description', '')

    def runtest(self):
        # Some custom test execution (dumb example follows).
        logger.debug("spec is： {}".format(self.spec))
        request = HttpRequest().initial(exception=YamlException, logger=logger)
        r = request.send_request(**self.spec)
        logger.info("results is: {}".format(r))
        self.assert_validate(r, self.spec.get('Validate'))
        self.response_extract(r, self.spec.get('Extract'))

    def response_extract(self, r, extract):
        if extract:
            get_result(r, extract)

    def assert_validate(self, r, validate):
        if validate:
            check_results(r, validate)

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            logger.critical(excinfo)
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.description}"


class YamlException(Exception):
    """Custom exception for error reporting."""


if __name__ == '__main__':
    pytest.main()
