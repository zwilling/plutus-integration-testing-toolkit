import unittest


class TestAlwaysSucceeds(unittest.TestCase):
    """
    Integration test case for the always succeeds example in https://github.com/input-output-hk/Alonzo-testnet/tree/main/resources/plutus-scripts
    """
    def test_build(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
