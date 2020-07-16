#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from tools.logger import log
from common.variable import is_vars


class RegExp(object):
    """正则相关类"""

    def __init__(self):
        self.re = re

    @classmethod
    def findall(cls, string):
        keys = re.findall(r"\{{(.*?)}\}", string)
        return keys

    @classmethod
    def subs(cls, keys, string):
        result = None
        if keys:
            log.info("提取变量：{}".format(keys))
            for i in keys:
                log.info("替换变量：{}".format(i))
                result = re.sub(r"\{{%s}}" % i, getattr(is_vars, i), string)
        log.info("替换结果：{}".format(result))
        return result

    def __call__(self, exp, string):
        return re.findall(r'\"%s":"(.*?)"' % exp, string)[0]


regexps = RegExp()

if __name__ == '__main__':
    pass
