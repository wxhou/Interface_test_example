#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t
import os
import yaml
import pytest
from requests import Response
from common.cache import cache
from common.json import dumps, loads
from common.request import HttpRequest
from common.regular import findalls, sub_var
from common.result import get_result, check_results
from common.exceptions import YamlException, RequestException
from utils.logger import logger


def pytest_collect_file(parent, path):
    if path.ext in (".yaml", ".yml") and path.basename.startswith("test"):
        return YamlFile.from_parent(parent, fspath=path)


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('unicode_escape').decode('utf-8')
        item._nodeid = item.nodeid.encode('unicode_escape').decode('utf-8')


class YamlFile(pytest.File):

    def collect(self):
        raw = yaml.safe_load(self.fspath.open(encoding='utf-8'))
        if variable := raw.get('GlobalVariable'):
            for k, v in variable.items():
                cache.set(k, v)
        if configuration := raw.get('Configuration'):
            configuration_str = dumps(configuration)
            keys = findalls(configuration_str)
            config = loads(sub_var({k: cache.get(k)
                           for k in keys}, configuration_str))
            cache.set('config', config)
        if not any("Test" in key for key in raw.keys()):
            raise YamlException(os.path.basename(self.fspath), raw.keys())
        for key in raw.keys():
            if not key.startswith('Test'):
                continue
            for name, spec in raw[key].items():
                yield YamlTest.from_parent(self,
                                           name=spec.get(
                                               'description') or name,
                                           spec=spec)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec
        self.request = HttpRequest(exception=(Exception, RequestException))

    def runtest(self):
        # Some custom test execution (dumb example follows).
        r = self.request.send_request(**self.spec)
        self.response_handle(r, self.spec.get('Validate'), self.spec.get('Extract'))

    def response_handle(self, r: Response, validate: t.Dict, extract: t.List):
        if validate:
            check_results(r, validate)
        if extract:
            get_result(r, extract)

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        logger.critical(excinfo.value)
        logger.critical(excinfo.traceback[-3:-1])

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"


if __name__ == '__main__':
    pytest.main()
