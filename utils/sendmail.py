#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import os
import zmail
import settings
from common.readconfig import conf




class Send:
    def __init__(self):
        self.report_path = os.path.join(settings.BASE_DIR, 'report.html')

    def __call__(self, *args, **kwargs):
        with open(self.report_path) as f:
            content_html = f.read()
        try:
            mail = {
                'from': '侯伟轩',
                'subject': '<%s>接口测试结果' % conf.host,
                'content_html': content_html,
                'attachments': [self.report_path, ]
            }
            server = zmail.server(
                conf.user,
                conf.pwd,
                smtp_host=conf.email,
                smtp_port=int(conf.port)
            )
            server.send_mail(conf.cont, mail)
        except Exception as e:
            print("邮件无法发送：{}".format(e))
        else:
            print("邮件发送成功")
