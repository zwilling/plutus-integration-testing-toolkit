import os
import unittest

from src.environment import TestkitEnvironment
from src.shell_utils import *


class TestAlwaysSucceeds(unittest.TestCase):
    """
    Integration test case for the always succeeds example in https://github.com/input-output-hk/Alonzo-testnet/tree/main/resources/plutus-scripts
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.env = TestkitEnvironment()

        # setup variables for testing a particular script:
        # path to the root folder of your code (where you want to run cabal for building)
        cls.code_folder = cls.env.repository_path + "/src/examples/Alonzo-testnet/resources/plutus-sources/"
        # name of the executable in your cabal.project
        cls.cabal_executable = "plutus-alwayssucceeds"
        # destination file for the compiled .plutus
        cls.compiled_file = "alwayssucceeds.plutus"
        # additional parameters for the plutus script
        cls.parameters = "42"

        cls.script_address = cls.compiled_file + ".addr"

    @classmethod
    def tearDownClass(cls) -> None:
        os.chdir(cls.env.repository_path)

    def setUp(self) -> None:
        os.chdir(self.code_folder)

    def test_build_preparation(self):
        # preparing build
        command = "cabal build -w ghc"
        success, message = run_command(command)
        self.assertTrue(success or "No targets given" in message, format_shell_error(command, message))

    def test_build_of_executable(self):
        # building executable
        command = build_command("cabal run", self.cabal_executable, "--", self.parameters, self.compiled_file)
        success, message = run_command(command)
        self.assertTrue(success, format_shell_error(command, message))
        self.assertTrue(os.path.exists(self.cabal_executable))

    def test_build_of_script_address(self):
        # building script address
        command = build_command(self.env.cardano_cli, "address", "build", "--payment-script-file", self.compiled_file,
                                "--testnet-magic", self.env.magic, "--out-file", self.script_address)
        success, message = run_command(command)
        self.assertTrue(success, format_shell_error(command, message))
        self.assertTrue(os.path.exists(self.script_address))


if __name__ == '__main__':
    unittest.main()
