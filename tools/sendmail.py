#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import os
import zmail
from config import conf
from common.readconfig import ini


def send_mail():
    with open(conf.REPORT_PATH) as f:
        content_html = f.read()
    try:
        mail = {
            'from': '侯伟轩',
            'subject': '<%s>接口测试结果' % conf.host,
            'content_html': content_html,
            'attachments': [
                ini.REPORT_PATH,
            ]
        }
        server = zmail.server(ini.user,
                              ini.pwd,
                              smtp_host=ini.email,
                              smtp_port=int(ini.port))
        server.send_mail(ini.cont, mail)
    except Exception as e:
        print("邮件无法发送：{}".format(e))
    else:
        print("邮件发送成功")
