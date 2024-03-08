import string

import bitcoin
from Crypto.Util import number
from bitcoin import *
from bitcoin.core import b2x
from bitcoin.wallet import CBitcoinSecret

from address import Address
from transaction import create_txin, create_txout, create_signed_transaction_p2pkh, create_signed_transaction_p2sh
import requests

class Wallet:
    def __init__(self, testnet=True):
        self.testnet = testnet
        self.address = Address(testnet)

    def get_transaction_details(self, txid: string):
        explorer_url = 'https://api.blockcypher.com/v1/btc/test3/txs'

        # Make a request to the blockchain explorer API
        api_url = f'{explorer_url}/{txid}'
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            tx_data = response.json()

            # Extract relevant information from the transaction data
            tx_hash = tx_data.get('hash')
            block_height = tx_data.get('block_height')
            confirmations = tx_data.get('confirmed')
            total_value = sum(output['value'] for output in tx_data.get('outputs', []))
            total_value_BTC = total_value/100000000

            # Print or use the extracted information as needed
            print(f'Transaction Hash: {tx_hash}')
            print(f'Block Height: {block_height}')
            print(f'Confirmations: {confirmations}')
            print(f'Total Value: {total_value} Satoshi')
            print(f'Total_value_BTC: {total_value_BTC} BTC')

            return tx_data
        else:
            print(f"Error: Unable to fetch transaction data. Status code: {response.status_code}")
            return None

    def get_address_details(self, address: string):
        explorer_url = 'https://api.blockcypher.com/v1/btc/test3/addrs'

        # Make a request to the blockchain explorer API
        api_url = f'{explorer_url}/{address}'
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            address_data = response.json()

            # Extract relevant information from the transaction data
            address_hash = address_data.get('address')
            total_receiver = address_data.get('total_receiver')
            total_sent = address_data.get('total_sent')
            total_balance = address_data.get('balance')
            total__final_balance = address_data.get('final_balance')
            total_value_BTC = total__final_balance / 100000000

            # Print or use the extracted information as needed
            print(f'Address Hash: {address_hash}')
            print(f'Total Receiver: {total_receiver}')
            print(f'Total Sent: {total_sent}')
            print(f'Total Balance: {total_balance} satoshi')
            print(f'Total_Balance_BTC: {total_value_BTC} BTC')

            return address_data
        else:
            print(f"Error: Unable to fetch transaction data. Status code: {response.status_code}")
            return None

    def spend_locked_fund(self, address: string, key: CBitcoinSecret, transaction_id: string, output_index: number,  destination_address: string, amount: number):
        if self.testnet:
            bitcoin.SelectParams('testnet')
        address_detail = self.get_address_details(address)
        txid = transaction_id
        output_index = output_index  # Index of the output in the transaction

        # Create a transaction input (TxIn)
        txin = create_txin(txid, output_index)

        # Create a transaction output to the desired destination
        final_balance = address_detail.get('final_balance')
        amount_to_send = amount  # Amount to send 0.00010000 Bitcoin
        txout1 = create_txout(amount_to_send, destination_address)

        # Create the transaction
        tx = create_signed_transaction_p2pkh(txin, txout1, key)  # Create the unsigned transaction

        print("Signed Transaction:", tx)
        print("Signed Transaction hex:", b2x(tx.serialize()))
        # # Broadcast the transaction
        # broadcast_tx(tx)

    def spend_locked_fund_multisig_address(self, keys: list, transaction_id: string, output_index: number, destination_address: string, amount: number):
        if self.testnet:
            bitcoin.SelectParams('testnet')

        address = self.address.create_addr_P2SH(keys)

        txid = transaction_id
        output_index = output_index  # Index of the output in the transaction

        # Create a transaction input (TxIn)
        txin = create_txin(txid, output_index)

        # Create a transaction output to the desired destination
        amount_to_send = amount  # Amount to send 0.00010000 Bitcoin
        txout = create_txout(amount_to_send, destination_address)

        # Create the transaction
        tx = create_signed_transaction_p2sh(txin, txout, keys, address['redeem_script'])  # Create the unsigned transaction

        # # Broadcast the transaction
        # broadcast_tx(tx)
