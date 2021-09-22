#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则相关操作类
"""
import re
import typing as t
from string import Template
from common.cache import cache
from common.json import is_json_str
from utils.logger import logger


def findalls(string: t.Text) -> t.Dict[t.Text, t.Any]:
    """查找所有"""
    key = re.compile(r"\${(.*?)\}").findall(string)
    res = {k: cache.get(k) for k in key}
    logger.debug("需要替换的变量：{}".format(res))
    return res


def sub_var(keys: t.Dict, string: t.Text) -> t.Text:
    """替换变量"""
    s = Template(string)
    res = s.safe_substitute(keys)
    logger.info("替换结果：{}".format(res))
    return res


def get_var(key: t.Text, raw_str: t.Text) -> t.Text:
    """获取变量"""
    if is_json_str(raw_str):
        return re.compile(r'\"%s":"(.*?)"' % key).findall(raw_str)[0]
    return re.compile(r'%s' % key).findall(raw_str)[0]
