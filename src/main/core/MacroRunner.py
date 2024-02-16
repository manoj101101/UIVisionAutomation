"""
***Macro Runner Module

*Using this module we can run our UI Vision macros automatically,
*Script can take care of running multiple macros
*It supports running the scripts via command line, so you can integrate it with Jenkins...
"""

__version__ = '1.0'
__author__ = 'Manoj Mathpal'

import argparse
import datetime
import os
import subprocess
import sys
import time
import Logger

logger = Logger.Logger.setup_logger()


# function to create a process for opening the browser...
def open_browser(browser_path, path, macro_params, incognito=False):
    args = (
            r'file:///' + macro_params['path_autorun_html'] +
            '?storage=xfile&loadmacrotree=0&macro=' + macro_params['macro'] +
            '&closeRPA=0&direct=1&savelog=' + path
    )
    proc = subprocess.Popen([browser_path, args])
    logger.info(
        f"Strated a parent process to open browser and run macro ::: '{macro_params['macro']}'")
    logger.info(
        f"Parent process id ::: '{proc.pid}'")
    return proc


# function to kill the browser process...
def close_browser(proc):
    logger.info(f" Killig Parent process pid : '{proc.pid}'")
    proc.kill()


def wait_for_completion(log_file_path, timeout_seconds):
    status_runtime = 0
    logger.info(f"Waiting for macro to finish the execution ::: Timeout value ::: '{timeout_seconds}'")
    while not os.path.exists(log_file_path) and status_runtime < timeout_seconds:
        time.sleep(1)
        status_runtime += 1
    return status_runtime < timeout_seconds


def check_macro_status(log_file_path, macro_name):
    with open(log_file_path) as f:
        status_text = f.readline()
        if 'Status=OK' in status_text:
            logger.info(
                f"Execution completed for macro ::: '{macro_name}' ::: Status :::  PASSED")
        else:
            logger.error(
                 f"Execution completed for macro ::: '{macro_name}' ::: Status :  FAILED")
            try:
                error_line = next(line.strip() for line in open(log_file_path) if '[error]' in line.lower())
                logger.error(
                    f"Error ::: '{error_line}'")
            except StopIteration:
                print(" ")
                logger.info(
                    f"Not able to find any error lines please re-verify the log file")
                logger.info(
                    f"Log File Location ::: {log_file_path}")
            return -1


def macrorunner(macro_params, log_file_path):
    assert os.path.exists(macro_params['path_autorun_html'])
    logger.info(
        f"Log File will be generated at location ::: {log_file_path}")
    try:
        if wait_for_completion(log_file_path, macro_params['timeout_seconds']):
            if check_macro_status(log_file_path, macro_params['macro']) == -1:
                return -1
        else:
            logger.error(
                f"Macro '{macro_params['macro']}' did not complete within the time given ::: {macro_params['timeout_seconds']} seconds")
            return -1
    except Exception as excep:
        logger.info(
            f"Exception occured during the execution of macro ::: '{macro_params['macro']}'")
        logger.error(
            f"'{excep}'")
        return -1


def macro_logs_setup(macro_name):
    logger.info(
        f" '{macro_name}' execution logs will be stored under UI Vision project directory in /logs folder")
    log_file = macro_name + '_logs_' + str(datetime.datetime.now().strftime("%m-%d-%Y_%H_%M_%S")) + '.txt'
    projectpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    log_folder = os.path.join(projectpath, 'logs/')

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file_path = log_folder + log_file
    return log_file_path


# function run macros...
def run_macros(args):
    is_run_successful = 0
    user_path = os.path.expanduser('~')
    macro_names = args.macro
    default_params = {
        'timeout_seconds': 100,
        'path_autorun_html': user_path + '/Downloads/ui.vision.html',
        'browser_path': '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    }

    for macro_name in macro_names:
        logger.info(
            f"Running Macro ::: ************'{macro_name}'*************")
        logger.info(
            f"Default Params ::: browser path ::: '{default_params['browser_path']}' ::: autorun html file path ::: '{default_params['path_autorun_html']}'")
        log_file_path = macro_logs_setup(macro_name)
        browser_proc = open_browser(default_params['browser_path'], log_file_path,
                                    {'macro': macro_name, 'path_autorun_html': default_params['path_autorun_html']},
                                    args)
        stat = macrorunner({'macro': macro_name, **default_params, 'incognito': args.incognito}, log_file_path)
        if stat == -1:
            is_run_successful = -1
        close_browser(browser_proc)

    return is_run_successful


# main thread initializiation...
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run multiple UI-Vision macros.')
    parser.add_argument('--macro', type=str, nargs='+', help='Names of the macros to run')
    parser.add_argument('--incognito', action='store_true', help='Open Chrome in incognito mode')

    cmd_args = parser.parse_args()
    logger.info(f"Parameters passed ::: macro name ::: '{cmd_args.macro}'")

    flag = (run_macros(cmd_args))
    sys.exit(flag)
