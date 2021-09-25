import re

from src.shell_utils import *
from src.environment import TestkitEnvironment


def get_utxo_in_wallet(env):
    """
    Finds a utxo at in the wallet

    :param env: environment variables
    :type env: TestkitEnvironment
    :return: utxo id
    """
    command = build_command(env.cardano_cli, "query", "utxo", "--address", "$(cat " + env.wallet_payment_addr + ")",
                            "--testnet-magic", env.magic)
    success, message = run_command(command)
    lines = message.split("\\n")
    if len(lines) <= 2:
        raise Exception("Could not find utxo with " + command + " in\n " + format_shell_error(command, message))

    # TODO: smarter selection than just using the first one
    # parse while handling multiple whitespaces
    first_utxo_line = re.sub(" +", " ", lines[2]).split(" ")
    utxo = first_utxo_line[0] + "#" + first_utxo_line[1]
    return utxo


def query_pparams(env):
    """
    preparing the pparams
    """
    command = build_command(env.cardano_cli, "query", "protocol-parameters",
                            "--testnet-magic", env.magic,
                            "--out-file", "pparams.json")
    success, message = run_command(command)
