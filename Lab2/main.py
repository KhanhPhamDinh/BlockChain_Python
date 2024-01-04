import os

import bitcoin as bitcoin

from wallet import Wallet

if __name__ == '__main__':
    wallet = Wallet(True)
    wallet.create_addr_P2PKHB(os.urandom(32))

