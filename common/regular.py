#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则相关操作类
"""
import re
import logging
from common.cache import cache
from utils.serializer import is_json_str


logger = logging.getLogger('debug')


def findalls(string):
    """查找所有"""
    key = re.compile(r"\{{(.*?)}\}").findall(string)
    return key


def sub_var(keys, string):
    """替换变量"""
    result = None
    for i in keys:
        logger.info("替换变量：{}".format(i))
        result = re.compile(r"\{{%s}}" % i).sub(cache[i], string)
    logger.info("替换结果：{}".format(result))
    return result


def get_var(key, raw_str):
    """获取"""
    if is_json_str(raw_str):
        return re.compile(r'\"%s":"(.*?)"' % key).findall(raw_str)[0]
    return re.compile(r'%s' % key).findall(raw_str)[0]


if __name__ == '__main__':
    pass
