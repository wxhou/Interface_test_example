#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import allure
import urllib3
import logging
from requests import Session
from requests.exceptions import RequestException
from common.ApiData import testinfo
from common.RegExp import regexps
from common.result import get_result
from utils.serializer import loads, dumps


urllib3.disable_warnings()

logger = logging.getLogger('debug')


class HttpRequest(Session):
    """requests方法二次封装"""

    def __init__(self, *args, **kwargs):
        super(HttpRequest, self).__init__(*args, **kwargs)
        self.timer = None
        self.timeout = 30.0
        self.headers = testinfo.test_info('headers')

    def __call__(self, *args, **kwargs):
        return self.send_request(*args, **kwargs)

    def send_request(self, method: str, route: str, extract: str, **kwargs):
        """发送请求
        :param method: 发送方法
        :param route: 发送路径
        optional 可选参数
        :param extract: 要提取的值
        :param params: 发送参数-"GET"
        :param data: 发送表单-"POST"
        :param json: 发送json-"post"
        :param headers: 头文件
        :param cookies: 验证字典
        :param files: 上传文件,字典：类似文件的对象``
        :param timeout: 等待服务器发送的时间
        :param auth: 基本/摘要/自定义HTTP身份验证
        :param allow_redirects: 允许重定向，默认为True
        :type bool
        :param proxies: 字典映射协议或协议和代理URL的主机名。
        :param stream: 是否立即下载响应内容。默认为“False”。
        :type bool
        :param verify: （可选）一个布尔值，在这种情况下，它控制是否验证服务器的TLS证书或字符串，在这种情况下，它必须是路径到一个CA包使用。默认为“True”。
        :type bool
        :param cert: 如果是字符串，则为ssl客户端证书文件（.pem）的路径
        :return: request响应
        """
        method = method.upper()
        url = testinfo.test_info('url') + route
        try:
            logger.info("Request Url: {}".format(url))
            logger.info("Request Method: {}".format(method))
            if kwargs:
                kwargs_str = dumps(kwargs)
                is_sub = regexps.findall(kwargs_str)
                if is_sub:
                    kwargs = dumps(regexps.subs(is_sub, kwargs_str))
            logger.info("Request Data: {}".format(kwargs))
            response = self.dispatch(method, url, **kwargs)
            self.timer = response.elapsed.total_seconds()  # timer
            description_html = f"""
            <font color=red>请求方法:</font>{method}<br/>
            <font color=red>请求地址:</font>{url}<br/>
            <font color=red>请求头:</font>{str(response.headers)}<br/>
            <font color=red>请求参数:</font>{json.dumps(kwargs,
                                                    ensure_ascii=False)}<br/>
            <font color=red>响应状态码:</font>{str(response.status_code)}<br/>
            <font color=red>响应时间:</font>{str(self.timer)}<br/>
            """
            allure.dynamic.description_html(description_html)
            logger.info(response)
            logger.info("Response Data: {}".format(response.text))
            if extract:
                get_result(response, extract)
            return response
        except RequestException as e:
            logger.error(format(e))
        except Exception as e:
            raise e

    def dispatch(self, method, *args, **kwargs):
        handler = getattr(self, method.lower())
        return handler(*args, **kwargs)


req = HttpRequest()
