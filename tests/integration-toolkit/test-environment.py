import os
import unittest
import subprocess

from src.environment import TestkitEnvironment


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.env = TestkitEnvironment()

    def test_loading_env(self):
        for field in [self.env.socket, self.env.cardano_cli, self.env.magic]:
            self.assertIsNotNone(field, "Should be able to load environment variables")

    def test_socket_available(self):
        print("socket", self.env.socket)
        self.assertTrue(os.path.exists(self.env.socket), "Your socket config is not pointing to a running cardano-node")

    def test_cli_available(self):
        cli = self.env.cardano_cli
        if cli.startswith("/"):
            self.assertTrue(os.path.exists(self.env.cardano_cli), "Your cardano-cli could not be found, check the environment-setup.sh")
        else:
            # check if it is executable
            result = subprocess.check_output([cli, "--version"])
            self.assertTrue("cardano-cli" in str(result), cli + "should be available")


if __name__ == '__main__':
    unittest.main()
