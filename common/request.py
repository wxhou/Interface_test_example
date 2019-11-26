#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import requests
from utils.logger import log
from requests.auth import AuthBase
from requests.exceptions import RequestException
from common.readconfig import conf


class PizzAuth(AuthBase):
    """身份令牌"""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'JWT ' + self.token
        return r


def get(url, headers=None, params=None, auth=None):
    """
    GET请求
    :param url:
    :param headers:
    :param params:
    :return:
    """
    try:
        response = requests.get(url=url,
                                headers=headers,
                                params=params,
                                auth=auth,
                                timeout=float(conf.timeout))
    except RequestException as e:
        log.exception(format(e))
    except Exception as e:
        log.exception(format(e))
    else:
        #  response.elapsed.total_seconds()  返回当前接口所用的秒数
        #  response.elapsed.total_seconds() / 1000  返回当前接口所用的毫秒数
        return response


def post(url, data=None, headers=None, files=None, auth=None):
    """
    POST请求
    :param url:
    :param data:
    :param headers:
    :param files: 上传文件
    :return:
    """
    try:
        response = requests.post(url=url,
                                 data=data,
                                 headers=headers,
                                 files=files,
                                 auth=auth,
                                 timeout=float(conf.timeout))
    except RequestException as e:
        log.exception(format(e))
    except Exception as e:
        log.exception(format(e))
    else:
        return response
        #  response.elapsed.total_seconds()  返回当前接口所用的秒数
        #  response.elapsed.total_seconds() / 1000  返回当前接口所用的毫秒数


if __name__ == '__main__':
    pass
