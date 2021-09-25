# plutus-integration-testing-toolkit
A toolkit for integration testing of smart contracts written in Plutus for the Cardano blockchain

This repository was started as part of the [Plutus Pioneer Capstone challenge #2](https://ucarecdn.com/8f27865c-f861-458e-bc97-ad13be9f3633/CardanoSummit2021_PlutusPioneerCapstone.pdf)

For smart contract development it is especially important that the resulting code works correctly. To ensure this it is very helpful to run integration tests.
They include compilation, building transactions, submitting transactions and checking if the result on the blockchain is as expected.
This frameworks lets you write tests in python unittests and run them on the cardano blockchain.

## Overview
:memo: Add 5m outline video
Requirements: Linux, Mac or Windows setup to run bash and Python3 (for example WSL)

## Installation
1. Configure the variables in **environment-setup.sh** to tell the toolkit where to find your cardano-node, cli, testnet-magic etc.
2. Setup a Python3 venv for running the tests (using venv)
```bash
cd plutus-integration-testing-toolkit
python3 -m venv venv
```
3. Make sure you have the example code by cloning the git submodules
```bash
git submodule update -i
```
4. Setup the wallet for testing in the wallet folder 

## Usage and Examples
1. Load your nix environment for building Plutus code with cabal
2. run test script
```bash
./run-tests.sh
```
To test your own scripts instead of the examples, you can create a new test file by copying one of the examples in tests/examples and adjust the parameters and test cases to your liking.

## Test cases
- integration-toolkit/test-environment: checks whether your environment config looks correct and if the cli can query the testnet tip
For each smart contract to test (an example for alwayssucceeds is given)
  - if the code builds
  - if the executable build
  - if the script address can be created
  - if the datum hash can be build
  - if the transaction can be build
  - if the transaction can be signed and submitted
