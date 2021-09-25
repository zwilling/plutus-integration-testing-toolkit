"""
Utility functions for running shell commands and returning the output and success state
"""

import subprocess


class BColors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def build_command(*args):
    """

    :param args: string arguments to concatinate
    :return: command as string
    """
    res = str()
    for arg in args:
        res += str(arg) + " "
    return res


def run_command(command):
    """
    Tries running a command and collects information whether the command was successful and the output
    (stdout in case of success, stderr in case of failure)

    :param command: the command to run
    :type command: str
    :return: success?, output of the result or the error string
    :rtype: bool, str
    """
    try:
        # check if command needs to be split into arguments:
        # if " " in command:
        #     command = command.split(" ")
        # print("!command", command)
        completed_process = subprocess.run(command, capture_output=True, shell=True)
    except subprocess.CalledProcessError as error:
        # caught error
        return False, error.output
    if completed_process.returncode == 0:
        return True, str(completed_process.stdout)
    else:
        return False, str(completed_process.stderr)


def format_shell_error(command, error):
    """
    Formats a error from shell to be displayed properly

    :param command: the command that was run
    :param error: error as returned from subprocess.run()
    :return:
    """
    return BColors.FAIL + "Command " + command + " failed with:\n" + str(error).replace("\\n", "\n") + BColors.ENDC

