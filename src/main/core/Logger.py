import logging
import os
import sys


class Logger:

    @staticmethod
    def setup_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]')

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.info(
            f"\nLogger Initialized :  Stream Logger : logs will be visible on console\n")
        return logger


def get_logger(self):
    return self.logger
