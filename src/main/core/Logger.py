import logging
import os
import sys


class Logger:


    def setup_logger(log_file):
        projectpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))));

        log_folder = os.path.join(projectpath, 'logs')

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_file_path = os.path.join(log_folder, log_file)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - [%(threadName)-12.12s] - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler(sys.stdout);
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger, log_file_path


def get_logger(self):
    return self.logger

