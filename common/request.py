#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import urllib3
from requests.exceptions import RequestException
from common.readconfig import ini
from utils.log import logger

urllib3.disable_warnings()


class Request:
    def __init__(self):
        self.requests = requests
        self.timeout = float(ini.timeout)
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    def get(self, *args, **kwargs):
        """
        get请求
        :param args: url headers params auth
        :param kwargs:
        """
        try:
            response = self.requests.get(*args, **kwargs,
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
        :param args: url data headers files
        :param kwargs:
        """
        try:
            response = self.requests.post(*args, **kwargs,
                                          headers=self.headers,
                                          timeout=self.timeout)
            return response
        except RequestException as e:
            logger.exception(format(e))
        except Exception as e:
            raise e


request = Request()
