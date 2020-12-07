#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import allure
import urllib3
import requests
from requests.exceptions import RequestException
from core.serialize import deserialization, serialization
from core.getresult import get_result
from common.ApiData import testinfo
from common.RegExp import regexps
from utils.logger import Logger

urllib3.disable_warnings()

log = Logger(__name__).logger


class HttpRequest(object):
    """requests方法二次封装"""

    http_method_names = 'get', 'post', 'put', 'delete', 'patch', 'head', 'options'

    def __init__(self):
        self.timer = None
        self.timeout = 30.0
        self.r = requests.session()
        self.headers = testinfo.test_info('headers')

    def __call__(self, *args, **kwargs):
        return self.request(*args, **kwargs)

    def request(self, method: str, route: str, extract: str, **kwargs):
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
            log.info("Request Url: {}".format(url))
            log.info("Request Method: {}".format(method))
            if kwargs:
                kwargs_str = serialization(kwargs)
                is_sub = regexps.findall(kwargs_str)
                if is_sub:
                    new_kwargs_str = deserialization(
                        regexps.subs(is_sub, kwargs_str))
                    kwargs = new_kwargs_str
            log.info("Request Data: {}".format(kwargs))

            def dispatch(method, *args, **kwargs):
                if method.lower() in self.http_method_names:
                    handler = getattr(self.r, method.lower())
                    return handler(*args, **kwargs)
                else:
                    raise AttributeError("send request method is ERROR!")
            response = dispatch(method, url, **kwargs)
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
            log.info(response)
            log.info("Response Data: {}".format(response.text))
            if extract:
                get_result(response, extract)
            return response
        except RequestException as e:
            log.exception(format(e))
        except Exception as e:
            raise e


req = HttpRequest()
