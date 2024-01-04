import os
import string

import bitcoin
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

class Wallet:
    def __init__(self, testnet=True):
        self.testnet = testnet

    def key_to_addr(self, key: string):
        if self.testnet:
            bitcoin.SelectParams('testnet')

        # Generate a random private key
        private_key = CBitcoinSecret.from_secret_bytes(key)
        # Derive the public key and Bitcoin address
        public_key = private_key.pub
        address = P2PKHBitcoinAddress.from_pubkey(public_key)
        print("Generated Private Key:", private_key)
        print("Derived Public Key:", public_key.hex())
        print("Corresponding Bitcoin Address:", address)
