#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from common.GlobalVariable import var


class RegExp(object):
    """正则相关类"""

    def __init__(self):
        self.re = re

    @classmethod
    def findall(cls, string):
        return re.findall(r"\{{(.*?)}\}", string)

    def sub(self, string):
        for i in self.findall(string):
            re.sub(r"\{{%s}}" % i, getattr(var, i), string)

    def __call__(self, exp, string):
        return re.findall(r'\"%s":"(.*?)"' % exp, string)[0]


regexps = RegExp()

if __name__ == '__main__':
    pass
