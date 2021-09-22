#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则相关操作类
"""
import re
from string import Template
from common.cache import cache
from common.json import is_json_str
from utils.logger import logger


def findalls(string):
    """查找所有"""
    key = re.compile(r"\${(.*?)\}").findall(string)
    res = {k: cache.get(k) for k in key}
    logger.debug("需要替换的变量：{}".format(res))
    return res


def sub_var(keys, string):
    """替换变量"""
    s = Template(string)
    res = s.safe_substitute(keys)
    logger.info("替换结果：{}".format(res))
    return res


def get_var(key, raw_str):
    """获取变量"""
    if is_json_str(raw_str):
        return re.compile(r'\"%s":"(.*?)"' % key).findall(raw_str)[0]
    return re.compile(r'%s' % key).findall(raw_str)[0]
