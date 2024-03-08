import string

import bitcoin
from bitcoin.core import CScript
from bitcoin.core.script import OP_2, OP_CHECKMULTISIG, OP_0
from bitcoin.wallet import P2PKHBitcoinAddress, CBitcoinSecret, P2SHBitcoinAddress


class Address:
    def __init__(self, testnet=True):
        self.testnet = testnet

    def create_addr_P2PKH(self, key: string):
        if self.testnet:
            bitcoin.SelectParams('testnet')
        # Generate a random private key
        private_key = CBitcoinSecret.from_secret_bytes(key)
        # Derive the public key and Bitcoin address
        public_key = private_key.pub
        address = P2PKHBitcoinAddress.from_pubkey(public_key)
        return {'private_key': private_key, 'public_key': public_key, 'address': address}

    def create_addr_P2SH(self, keys: list):
        if self.testnet:
            bitcoin.SelectParams('testnet')
        bytes_CScript = list()
        bytes_CScript.append(OP_0)
        bytes_CScript.append(OP_2)
        for key in keys:
            private_key = CBitcoinSecret.from_secret_bytes(key);
            public_key = private_key.pub
            print("Private Key:", private_key)
            bytes_CScript.append(public_key)
        bytes_CScript.append(OP_2)
        bytes_CScript.append(OP_CHECKMULTISIG)

        redeem_script = CScript(bytes_CScript)
        address = P2SHBitcoinAddress.from_redeemScript(redeem_script)
        print("Redeem Script:", redeem_script)
        print("Multisig Address:", address)
        return {'redeem_script': redeem_script, 'multisig_address': address}

