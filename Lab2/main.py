import os

from wallet import Wallet

if __name__ == '__main__':
    wallet = Wallet()
    wallet.key_to_addr(os.urandom(32))

