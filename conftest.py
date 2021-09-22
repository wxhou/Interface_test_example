#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import json
import yaml
import pytest
import pytest
import logging
from string import Template
from common.cache import cache
from common.request import HttpRequest
from common.result import get_result, check_results
from utils.logger import logger


# def pytest_configure(config):
    # config.option.log_file = os.path.join(basedir, 'logs', 'server.log')


def pytest_collect_file(parent, path):
    if path.ext in (".yaml", ".yml") and path.basename.startswith("test"):
        logger.debug("pytest_collect_file is: {} {}".format(parent, path))
        return YamlFile.from_parent(parent, fspath=path)


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('unicode_escape').decode('utf-8')
        item._nodeid = item.nodeid.encode('unicode_escape').decode('utf-8')


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
            yield YamlTest.from_parent(self, name=spec.get('description') or name, 
                                       spec=spec)

class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec
        self.description = self.spec.get('description', '')

    def runtest(self):
        # Some custom test execution (dumb example follows).
        request = HttpRequest().initial(exception=YamlException, logger=logger)
        r = request.send_request(**self.spec)
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
            logger.critical(format(excinfo))
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
