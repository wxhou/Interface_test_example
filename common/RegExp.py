#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from core.serialize import is_json_str
from common.variable import is_vars
from utils.logger import log


class RegExp(object):
    """正则相关类"""

    def __init__(self):
        self.reg = re.compile

    def findall(self, string):
        key = self.reg(r"\{{(.*?)}\}").findall(string)
        return key
        
    def subs(self, keys, string):
        result = None
        for i in keys:
            log.info("替换变量：{}".format(i))
            result = self.reg(r"\{{%s}}" % i).sub(is_vars[i], string)
        log.info("替换结果：{}".format(result))
        return result

    def __call__(self, exp, string):
        if is_json_str(string):
            return self.reg(r'\"%s":"(.*?)"' % exp).findall(string)[0]
        return self.reg(r'%s' % exp).findall(string)[0]


regexps = RegExp()

if __name__ == '__main__':
    pass
