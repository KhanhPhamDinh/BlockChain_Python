import hashlib


class Transaction:
    def __init__(self, data: bytes):
        self.data = data

    def calculate_hash(self):
        return hashlib.sha256(self.data).hexdigest()
