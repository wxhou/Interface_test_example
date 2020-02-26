#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import urllib3
from requests.exceptions import RequestException
from common.readconfig import ini
from utils.log import logger

urllib3.disable_warnings()


class MyAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'JWT ' + self.token
        return r


class Request:
    def __init__(self):
        self.requests = requests
        self.timeout = float(ini.timeout)
        self.headers = {
            'User-Agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }

    def get(self, *args, **kwargs):
        """
        get请求
        :param args: url headers params auth
        :param kwargs:
        """
        try:
            response = self.requests.get(*args,
                                         **kwargs,
                                         headers=self.headers,
                                         timeout=self.timeout)
            return response
        except RequestException as e:
            logger.exception(format(e))
        except Exception as e:
            raise e

    def post(self, *args, **kwargs):
        """
        POST请求
        :param args: url data json headers files
        :param kwargs:
        """
        try:
            response = self.requests.post(*args,
                                          **kwargs,
                                          headers=self.headers,
                                          timeout=self.timeout)
            return response
        except RequestException as e:
            logger.exception(format(e))
        except Exception as e:
            raise e

    def session(self, url, cookies_data, **kwargs):
        """
        会话对象
        :param url:
        :param cookies_data:
        """
        if isinstance(cookies_data, dict):
            try:
                response = self.requests.session()
                response.get(url, timeout=self.timeout, **kwargs)
                cookie = self.requests.cookies.RequestsCookieJar()
                for i in cookies_data:
                    cookie.set(i, cookies_data[i])
                response.cookies.update(cookie)
                return response
            except requests.RequestException as e:
                logger.exception(e)
            except Exception as e:
                raise format(e)
        raise AttributeError("session cookies_data type is not Dict : {}".format(
            type(cookies_data)))


request = Request()

if __name__ == "__main__":
    pass