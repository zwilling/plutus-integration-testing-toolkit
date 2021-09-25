import os


class TestkitEnvironment:
    """
    Loading and handling the environment variables for using cardano
    """

    def __init__(self):
        self.__env = os.environ
        self.repository_path = os.getcwd()

    @property
    def socket(self):
        return self.__env.get("CARDANO_NODE_SOCKET_PATH")

    @property
    def magic(self):
        return self.__env.get("CARDANO_MAGIC")

    @property
    def cardano_cli(self):
        return self.__env.get("CARDANO_CLI")

    @property
    def wallet_payment_addr(self):
        return self.__env.get("WALLET_PAYMENT_ADDR")

    @property
    def wallet_sign_key(self):
        return self.__env.get("WALLET_SIGN_KEY")
