"""
日志类
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from main import basedir


def init_logger():
    """初始化日志"""

    logger_formatter = logging.Formatter(
        '%(levelname)s %(asctime)s [%(filename)s:%(lineno)s] %(thread)d %(message)s')
    debug_file = os.path.join(basedir, 'logs', 'server.log')

    # debug
    logger_debug = logging.getLogger(__name__)
    handler_debug = RotatingFileHandler(debug_file,
                                        encoding='utf-8',
                                        maxBytes=20 * 1024 * 1024,
                                        backupCount=10)
    handler_debug.setFormatter(logger_formatter)
    logger_debug.setLevel(logging.DEBUG)
    logger_debug.addHandler(handler_debug)
    return logger_debug


logger = init_logger()

if __name__ == '__main__':
    logger.debug("debug")
    logger.info("info")
    logger.warning('warning')
    logger.error("error")
    logger.critical('critical')
