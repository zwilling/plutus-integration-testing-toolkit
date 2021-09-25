#!/bin/bash
# Environment setup for how the toolkit can operate on your machine

# executable or path to your cardano-cli binary
export CARDANO_CLI=cardano-cli

# testnet magic to use (default 1097911063 for public testnet)
export CARDANO_MAGIC=1097911063

# Path to the socket connecting cardano-cli to the cardano-node
# For simplicity, I recommend using the socket provided by the node of the Daedalus wallet for the testnet
export CARDANO_SOCKET=~/.local/share/Daedalus/testnet/cardano-node.socket
