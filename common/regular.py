#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import logging
from common.cache import cache
from utils.serializer import is_json_str


logger = logging.getLogger('debug')


class Operation(object):
    """正则相关操作类"""

    def __init__(self):
        self.re = re.compile

    def findall(self, string):
        key = self.re(r"\{{(.*?)}\}").findall(string)
        return key

    def subs(self, keys, string):
        result = None
        for i in keys:
            logger.info("替换变量：{}".format(i))
            result = self.re(r"\{{%s}}" % i).sub(cache[i], string)
        logger.info("替换结果：{}".format(result))
        return result

    def get(self, key, string):
        """获取"""
        if is_json_str(string):
            return self.re(r'\"%s":"(.*?)"' % key).findall(string)[0]
        return self.re(r'%s' % key).findall(string)[0]


if __name__ == '__main__':
    pass
