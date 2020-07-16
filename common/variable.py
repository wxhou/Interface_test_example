#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Variable(object):
    def __init__(self):
        super(Variable, self).__init__()


is_vars = Variable()

if __name__ == '__main__':
    setattr(is_vars, 'name', 'hoou')
    print(getattr(is_vars, 'name'))
