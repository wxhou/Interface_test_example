#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Variable(object):
    """全局变量池"""

    def __init__(self):
        self.vars = {}

    def __getitem__(self, key):
        return self.vars[key]

    def __setitem__(self, key, value):
        self.vars[key] = value

    def __delitem__(self, key):
        return self.vars.pop(key, None)

    def __len__(self):
        return len(self.vars)

    def __bool__(self):
        return bool(self.vars)

    def __contains__(self, key):
        return key in self.vars


is_vars = Variable()

if __name__ == '__main__':
    print(bool(is_vars))