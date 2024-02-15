import logging
import os
import sys


class Logger:

    @staticmethod
    def setup_logger(log_file):
        projectpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))));
        print("projectpath==")
        print(projectpath)
        log_folder = os.path.join(projectpath, 'logs')
        print("logfolder==")
        print(log_folder)

        # if not os.path.exists(log_folder):
        #     os.makedirs(log_folder)

        log_file_path = log_folder + log_file
        # log_file_path = os.path.join(log_folder, log_file)
        print("final log file path------>")
        print(log_file_path)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - [%(threadName)-12.12s] - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler(sys.stdout);
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger, log_file_path


def get_logger(self):
    return self.logger
