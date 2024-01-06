import os

import bitcoin as bitcoin

from wallet import Wallet

if __name__ == '__main__':
    key = b'\x9cF\xbd1\xf7\x18\xcd\x92\xacy\x02\xe1\xcf?#\x80NQ*\x81\xe1j \x1b\xfd\xfa*\xff\xdd\xd6\xfc\x06';
    wallet = Wallet(True)
    object_result = wallet.create_addr_P2PKH(key)
    print("Generated Private Key:", object_result['private_key'])
    print("Derived Public Key:", object_result['public_key'].hex())
    print("Corresponding Bitcoin Address:", object_result['address'])

    wallet.spend_locked_fund(object_result['private_key'])
