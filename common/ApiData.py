#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from ruamel import yaml
from config.conf import DATA_DIR


class ApiInfo:
    """接口信息"""

    def __init__(self):
        self.info_path = os.path.join(DATA_DIR, 'testinfo.yaml')
        self.business_path = os.path.join(DATA_DIR, 'BusinessInterface.yaml')
        self.stand_alone_path = os.path.join(DATA_DIR, 'stand_alone_interface.yaml')

    @classmethod
    def load(self, path):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @property
    def info(self):
        return self.load(self.info_path)

    @property
    def business(self):
        return self.load(self.business_path)

    @property
    def stand_alone(self):
        return self.load(self.stand_alone_path)

    def test_info(self, value):
        """测试信息"""
        return self.info['test_info'][value]

    def login_info(self, value):
        """登录信息"""
        return self.stand_alone['登录'][value]

    def case_info(self, name):
        """用例信息"""
        return self.business[name]

    def stand_info(self, name):
        """单个接口"""
        return self.stand_alone[name]


testinfo = ApiInfo()

if __name__ == '__main__':
    print(testinfo.info['test_info'])
