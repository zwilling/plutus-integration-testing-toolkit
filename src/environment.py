import os


class TestkitEnvironment:
    """
    Loading and handling the environment variables for using cardano
    """

    def __init__(self):
        self.__env = os.environ

    @property
    def socket(self):
        return self.__env.get("CARDANO_NODE_SOCKET_PATH")

    @property
    def magic(self):
        return self.__env.get("CARDANO_MAGIC")

    @property
    def cardano_cli(self):
        return self.__env.get("CARDANO_CLI")
