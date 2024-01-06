import string

import bitcoin
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from transaction import create_txin, create_txout, create_signed_transaction


class Wallet:
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
        return {'private_key': private_key, 'public_key': public_key, 'address' : address}

    def spend_locked_fund(self, key: string):
        if self.testnet:
            bitcoin.SelectParams('testnet')
        txid = "dbc04541769efd9819994d23e4d9cae08f0423e78a2b2b309c8513e62368ebfb"
        output_index = 0  # Index of the output in the transaction

        # Create a transaction input (TxIn)
        txin = create_txin(txid, output_index)

        # Create a transaction output to the desired destination
        destination_address = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'  # Recipient’s address
        amount_to_send = 0.0001 # Amount to send 0.00010000 Bitcoin
        txout = create_txout(amount_to_send, destination_address)

        # Create the transaction
        tx = create_signed_transaction(txin, txout, key)# Create the unsigned transaction

        # # Broadcast the transaction
        # broadcast_tx(tx)

