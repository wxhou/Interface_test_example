#!/usr/bin/env python3
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
import os
import configparser

config_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', 'config.ini')


class Config:
    SERVER = 'SERVER'
    SERVER_VALUE = 'url'
    SERVER_TIMEOUT = 'timeout'
    NAME_MAIL = 'MAIL'
    MAIL_VALUE_HOST = 'emailhost'
    MAIL_VALUE_PORT = 'emailport'
    MAIL_VALUE_USER = 'emailuser'
    MAIL_VALUE_PWD = 'emailpwd'

    CONTTACTS = 'CONTTACTS'

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(config_path)

    def get(self, option, name):
        return self.config.get(option, name)

    def set(self, option, name, value):
        self.config.set(option, name, value)
        with open(config_path, 'w') as f:
            self.config.write(f)

    @property
    def host(self):
        return self.get(Config.SERVER, Config.SERVER_VALUE)

    @host.setter
    def host(self, value):
        self.set(Config.SERVER, Config.SERVER_VALUE, value)

    @property
    def timeout(self):
        return self.get(Config.SERVER, Config.SERVER_TIMEOUT)

    @property
    def email(self):
        return self.get(Config.NAME_MAIL, Config.MAIL_VALUE_HOST)

    @property
    def port(self):
        return self.get(Config.NAME_MAIL, Config.MAIL_VALUE_PORT)

    @property
    def user(self):
        return self.get(Config.NAME_MAIL, Config.MAIL_VALUE_USER)

    @property
    def pwd(self):
        return self.get(Config.NAME_MAIL, Config.MAIL_VALUE_PWD)

    @property
    def cont(self):
        return [i[1] for i in self.config.items(Config.CONTTACTS)]


if __name__ == '__main__':
    a = Config()
    print(a.timeout)
