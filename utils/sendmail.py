#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File : sendmail.py
@Time : 2020-02-17 16:18:01
@Author : wxhou 
@Version : 1.0
@Contact : 1084502012@qq.com
'''
import sys
sys.path.append('.')
import os
import zmail
import settings
from common.readconfig import conf


def send_mail():
    with open(settings.REPORT_PATH) as f:
        content_html = f.read()
    try:
        mail = {
            'from': '侯伟轩',
            'subject': '<%s>接口测试结果' % conf.host,
            'content_html': content_html,
            'attachments': [
                settings.REPORT_PATH,
            ]
        }
        server = zmail.server(conf.user,
                              conf.pwd,
                              smtp_host=conf.email,
                              smtp_port=int(conf.port))
        server.send_mail(conf.cont, mail)
    except Exception as e:
        print("邮件无法发送：{}".format(e))
    else:
        print("邮件发送成功")
