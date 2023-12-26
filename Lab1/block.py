import hashlib
import json
from time import time

class Block:
    def __init__(self, transactions, prev_block_hash: bytes):
        self.timestamp = int(time())
        self.transactions = transactions
        self.prev_block_hash = prev_block_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_hashes = [trans.calculate_hash() for trans in self.transactions]
        concatenated_transactions = ''.join(transaction_hashes).encode()
        block_string = (str(self.prev_block_hash) + str(concatenated_transactions) + str(self.timestamp))

        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block - Timestamp: {self.timestamp}, Transactions: {self.transactions}, Hash: {self.hash[:20]}, " \
               f"Prev_block_hash: {self.prev_block_hash}"
