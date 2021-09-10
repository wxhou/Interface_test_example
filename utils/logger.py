#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler
from settings.settings import LOGGER_DIR


def init_logger(name):
    """初始化日志"""

    logger_formatter = logging.Formatter(
        '%(levelname)s %(asctime)s %(module)s [%(filename)s:%(lineno)s] %(thread)d %(message)s')
    debug_file = os.path.join(LOGGER_DIR, 'debug.log')
    error_file = os.path.join(LOGGER_DIR, 'error.log')

    # debug
    logger_debug = logging.getLogger(name)
    handler_debug = RotatingFileHandler(debug_file,
                                        encoding='utf-8',
                                        maxBytes=20 * 1024,
                                        backupCount=10)
    handler_debug.setFormatter(logger_formatter)
    logger_debug.setLevel(logging.DEBUG)
    logger_debug.addHandler(handler_debug)

    # error
    # logger_error = logging.getLogger('error')
    handler_error = RotatingFileHandler(error_file,
                                        encoding='utf-8',
                                        maxBytes=20 * 1024,
                                        backupCount=10)
    handler_error.setFormatter(logger_formatter)
    logger_debug.setLevel(logging.ERROR)
    logger_debug.addHandler(handler_debug)

    # 在控制台输出
    cmd_handler = logging.StreamHandler()
    cmd_handler.setFormatter(logger_formatter)
    loggers = logging.getLogger(__name__)
    loggers.setLevel(logging.INFO)
    loggers.addHandler(cmd_handler)


init_logger(__name__)
if __name__ == '__main__':
    logger = logging.getLogger('debug')
    logger.debug("你好 123")
    logger.error("你好 456")
    logger = logging.getLogger('error')
    logger.error("你好， 有错误")
