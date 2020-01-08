#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import os
import settings
import configparser


SERVER = 'SERVER'
SERVER_VALUE = 'url'
SERVER_TIMEOUT = 'timeout'
NAME_MAIL = 'MAIL'
MAIL_VALUE_HOST = 'emailhost'
MAIL_VALUE_PORT = 'emailport'
MAIL_VALUE_USER = 'emailuser'
MAIL_VALUE_PWD = 'emailpwd'
CONTTACTS = 'CONTTACTS'


class Config:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(settings.INI_PATH)

    def get(self, option, name):
        return self.config.get(option, name)

    def set(self, option, name, value):
        self.config.set(option, name, value)
        with open(settings.INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def host(self):
        return self.get(SERVER, SERVER_VALUE)

    @host.setter
    def host(self, value):
        self.set(SERVER, SERVER_VALUE, value)

    @property
    def timeout(self):
        return self.get(SERVER, SERVER_TIMEOUT)

    @property
    def email(self):
        return self.get(NAME_MAIL, MAIL_VALUE_HOST)

    @property
    def port(self):
        return self.get(NAME_MAIL, MAIL_VALUE_PORT)

    @property
    def user(self):
        return self.get(NAME_MAIL, MAIL_VALUE_USER)

    @property
    def pwd(self):
        return self.get(NAME_MAIL, MAIL_VALUE_PWD)

    @property
    def cont(self):
        return [i[1] for i in self.config.items(CONTTACTS)]


conf = Config()
if __name__ == '__main__':
    print(conf.timeout)
