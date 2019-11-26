#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import os
import yaml
import settings

route_path = os.path.join(settings.BASE_DIR, 'TestData', 'route.yaml')
payload_path = os.path.join(settings.BASE_DIR, 'TestData', 'payload.yaml')


class Route:
    """路径"""
    def __init__(self):
        with open(route_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        item_data = self.data.get(item)
        if item_data:
            return item_data
        else:
            raise ValueError("{} 路径不存在".format(item))


route = Route()


class Payload:
    """请求参数"""
    def __init__(self):
        with open(payload_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        return self.data.get(item)


payload = Payload()

if __name__ == '__main__':
    print(route.天气)
