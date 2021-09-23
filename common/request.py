"""
requests二次封装类
"""
import typing as t
import allure
import urllib3
from requests import Session, Response
from requests.exceptions import RequestException
from common.cache import cache
from common.json import json, loads, dumps
from common.regular import get_var, sub_var, findalls
from utils.logger import logger

urllib3.disable_warnings()


class HttpRequest(Session):
    """requests方法二次封装"""

    def __init__(self, *args: t.Union[t.Set, t.List], **kwargs: t.Dict[t.Text, t.Any]):
        super(HttpRequest, self).__init__()
        self.exception = kwargs.get("exception", Exception)

    def send_request(self, **kwargs: t.Dict[t.Text, t.Any]) -> Response:
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
        kwargs_str = dumps(kwargs)
        logger.info("request data: {}".format(kwargs))
        method = kwargs.get('method', 'GET').upper()
        url = cache.get('baseurl', default='') + kwargs.get('route')
        try:
            logger.info("Request Url: {}".format(url))
            logger.info("Request Method: {}".format(method))
            if is_sub := findalls(kwargs_str):
                kwargs = loads(sub_var(is_sub, kwargs_str))
            logger.info("Request Data: {}".format(kwargs))
            response = self.dispatch(method, url, **cache.get('config'),
                                     **kwargs.get('RequestData'))
            description_html = f"""
            <font color=red>请求方法:</font>{method}<br/>
            <font color=red>请求地址:</font>{url}<br/>
            <font color=red>请求头:</font>{str(response.headers)}<br/>
            <font color=red>请求参数:</font>{json.dumps(kwargs, ensure_ascii=False)}<br/>
            <font color=red>响应状态码:</font>{str(response.status_code)}<br/>
            <font color=red>响应时间:</font>{str(response.elapsed.total_seconds())}<br/>
            """
            allure.dynamic.description_html(description_html)
            logger.info("Request Result: {}".format(response))
            return response
        except RequestException as e:
            logger.error(format(e))
        except self.exception as e:
            raise e

    def dispatch(self, method: t.Text, *args: t.Union[t.List, t.Tuple], **kwargs: t.Dict) -> Response:
        """请求分发"""
        handler = getattr(self, method.lower())
        return handler(*args, **kwargs)
