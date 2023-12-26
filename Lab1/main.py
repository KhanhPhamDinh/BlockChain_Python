from block import Block
from transaction import Transaction

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tx1 = Transaction(b"Transaction data 1")
    tx2 = Transaction(b"Transaction data 2")

    block = Block([tx1, tx2], b"0")  # Assuming "0" as the previous block's hash for the first block
    print(block)

    # To get hash of a transaction
    print(f"Hash of tx1: {tx1.calculate_hash()}")
    print(f"Hash of tx2: {tx2.calculate_hash()}")
