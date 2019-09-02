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
import yaml

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
route_path = os.path.join(root_dir, 'data', 'route.yaml')
payload_path = os.path.join(root_dir, 'data', 'payload.yaml')


class Route:
    def __init__(self):
        with open(route_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        item_data = self.data.get(item)
        if item_data:
            return item_data
        else:
            raise TypeError("{} 路径不存在".format(item))


class Payload:
    def __init__(self):
        with open(payload_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        return self.data.get(item)


if __name__ == '__main__':
    rou = Payload()
    print(rou.test_001)
