#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler


basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def init_logger():
    """初始化日志"""

    logger_formatter = logging.Formatter(
        '%(levelname)s %(asctime)s %(module)s [%(filename)s:%(lineno)s] %(thread)d %(message)s')
    debug_file = os.path.join(basedir, 'logs', 'server.log')

    # debug
    logger_debug = logging.getLogger('apitest')
    handler_debug = RotatingFileHandler(debug_file,
                                        encoding='utf-8',
                                        maxBytes=20 * 1024,
                                        backupCount=10)
    handler_debug.setFormatter(logger_formatter)
    logger_debug.setLevel(logging.DEBUG)
    logger_debug.addHandler(handler_debug)
    # 在控制台输出
    cmd_handler = logging.StreamHandler()
    cmd_handler.setFormatter(logger_formatter)
    cmd_handler.setLevel(logging.DEBUG)
    logger_debug.addHandler(cmd_handler)
    return logger_debug


logger = init_logger()

if __name__ == '__main__':
    logger.debug("debug")
    logger.info("")
    logger.error("你好， 有错误")
