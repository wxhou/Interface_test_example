#!/usr/bin/env python
# coding=utf-8
'''
@File    :   request.py
@Time    :   2019/09/02 10:31:45
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''

import sys

sys.path.append('.')
import requests
from utils.logger import Log
from requests.auth import AuthBase
from requests.exceptions import RequestException
from common.readconfig import Config

log = Log().logger
conf = Config()


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
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            auth=auth,
            timeout=float(conf.timeout)
        )
    except RequestException as e:
        log.error(format(e))
    except Exception as e:
        log.error(format(e))
    else:
        response_dict = {}
        response_dict['url'] = response.url
        response_dict['code'] = response.status_code
        response_dict['headers'] = response.headers
        response_dict['text'] = response.text
        response_dict['content'] = response.content
        try:
            response_dict['json'] = response.json()
        except Exception as e:
            log.warning(format(e))
            response_dict['json'] = None
        response_dict['cookies'] = response.cookies
        response_dict['time_seconds'] = response.elapsed.total_seconds()
        response_dict['time_consuming'] = response.elapsed.total_seconds() / 1000
        response_dict['history'] = response.history
        return response_dict


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
                                 timeout=float(conf.timeout)
                                 )
    except RequestException as e:
        log.error(format(e))
    except Exception as e:
        log.error(format(e))
    else:
        response_dict = {}
        response_dict['url'] = response.url
        response_dict['code'] = response.status_code
        response_dict['headers'] = response.headers
        response_dict['text'] = response.text
        response_dict['content'] = response.content
        try:
            response_dict['json'] = response.json()
        except Exception as e:
            log.warning(format(e))
            response_dict['json'] = None
        response_dict['cookies'] = response.cookies
        response_dict['time_seconds'] = response.elapsed.total_seconds()
        response_dict['time_consuming'] = response.elapsed.total_seconds() / 1000
        response_dict['history'] = response.history
        return response_dict


if __name__ == '__main__':
    pass
