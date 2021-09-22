#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t
import yaml
import pytest
import pytest
from requests import Response
from common.cache import cache
from common.json import dumps, loads
from common.request import HttpRequest
from common.regular import findalls, sub_var
from common.result import get_result, check_results
from common.exceptions import YamlException
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
        if variable := raw.get('variable'):
            for k, v in variable.items():
                cache.set(k, v)
        if config := raw.get('config'):
            keys = findalls(dumps(config))
            config = loads(sub_var({k: cache.get(k)
                           for k in keys}, dumps(config)))
            for k, v in config.items():
                cache.set(k, v)
        if tests := raw.get('tests'):
            for name, spec in tests.items():
                yield YamlTest.from_parent(self,
                                           name=spec.get('description') or name,
                                           spec=spec)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec
        self.description = self.spec.get('description', '')

    def runtest(self):
        # Some custom test execution (dumb example follows).
        request = HttpRequest(exception=(Exception, YamlException))
        r = request.send_request(**self.spec)
        self.assert_validate(r, self.spec.get('Validate'))
        self.response_extract(r, self.spec.get('Extract'))

    def response_extract(self, r: Response, extract: t.List):
        if extract:
            get_result(r, extract)

    def assert_validate(self, r: Response, validate: t.Dict):
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


if __name__ == '__main__':
    pytest.main()
