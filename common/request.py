#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import json
import requests
from tools.log import logger
from requests.exceptions import RequestException
from common.requests_config import requests_config

requests.urllib3.disable_warnings()


class MyAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'JWT ' + self.token
        return r


def get(*args, **kwargs):
    """
    get请求
    :param args: url headers params auth
    :param kwargs:
    """
    try:
        r = requests.get(*args,
                         **kwargs,
                         headers=requests_config['headers'],
                         timeout=requests_config['timeout'])
        return json.loads(r.text)
    except requests.exceptions.RequestException as e:
        logger.exception(format(e))
    except Exception as e:
        raise e


def post(*args, **kwargs):
    """
    POST请求
    :param args: url data json headers files
    :param kwargs:
    """
    try:
        r = requests.post(*args,
                          **kwargs,
                          headers=requests_config['headers'],
                          timeout=requests_config['timeout'])
        return json.loads(r.text)
    except RequestException as e:
        logger.exception(format(e))
    except Exception as e:
        raise e


def session(url, cookies_data: dict, **kwargs):
    """
    会话对象
    :param url: 服务器地址
    :param cookies_data: cookies数据
    """
    try:
        response = requests.session()
        response.get(url, timeout=requests_config['timeout'], **kwargs)
        cookie = requests.cookies.RequestsCookieJar()
        for i in cookies_data:
            cookie.set(i, cookies_data[i])
        response.cookies.update(cookie)
        return response
    except requests.RequestException as e:
        logger.exception(e)
    except Exception as e:
        raise e


__all__ = ['requests', 'MyAuth', 'get', 'post', 'session']

if __name__ == "__main__":
    r = get(url='https://tx.yunjinginc.com/api/page/info/?bdg_id=551')
    txt = json.loads(r.text)
    print(txt)
