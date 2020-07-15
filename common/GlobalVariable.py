#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Variable(object):
    def __init__(self):
        super(Variable, self).__init__()


var = Variable()

if __name__ == '__main__':
    setattr(var, 'name', 'hoou')
    print(getattr(var, 'name'))
