import os

import bitcoin as bitcoin

from wallet import Wallet

if __name__ == '__main__':
    key = b'\x9cF\xbd1\xf7\x18\xcd\x92\xacy\x02\xe1\xcf?#\x80NQ*\x81\xe1j \x1b\xfd\xfa*\xff\xdd\xd6\xfc\x06';
    wallet = Wallet(True)
    object_result = wallet.address.create_addr_P2PKH(key)
    print("Private Key:", object_result['private_key'])
    print("Public Key:", object_result['public_key'].hex())
    print("Bitcoin Address:", object_result['address'])
    wallet.spend_locked_fund(object_result['address'], object_result['private_key'], "55f64c1146814dcea03181e55806d693774720be5a2fc1203aad067cf9c58101", 0, 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB', 0.0001)
    wallet.get_transaction_details('e34ba064ab0d968103798dba824db63a760e008dfbd43c28c992c5ccc1c670a6')
    wallet.get_address_details('n1rbQzjdkjA7geUhtNkiXKGDiT82gfF2Y6')

    #wallet.spend_locked_fund_multisig_address([key1, key2], 'f190373cbd00a71535e0720a75adc86bb91b16526061b8a76a32028ba067245f', 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

    # while True:
    #     object_result: dict
    #     address: dict
    #     wallet = Wallet(True)
    #     print("Options: 1 - Create Address P2PKH, 2 - Spend Locked Fund P2PKH, 3 - Create Address P2SH,4 - Spend Locked Fund P2SH,  5 - Exit")
    #     choice = input("Enter your choice: ")
    #
    #     if choice == '1':
    #         key = b'\x9cF\xbd1\xf7\x18\xcd\x92\xacy\x02\xe1\xcf?#\x80NQ*\x81\xe1j \x1b\xfd\xfa*\xff\xdd\xd6\xfc\x06';
    #         object_result = wallet.address.create_addr_P2PKH(key)
    #         print("Private Key:", object_result['private_key'])
    #         print("Public Key:", object_result['public_key'])
    #         print("Address Key:", object_result['address'])
    #     elif choice == '2':
    #         key = b'\x9cF\xbd1\xf7\x18\xcd\x92\xacy\x02\xe1\xcf?#\x80NQ*\x81\xe1j \x1b\xfd\xfa*\xff\xdd\xd6\xfc\x06';
    #         object_result = wallet.address.create_addr_P2PKH(key)
    #         wallet.spend_locked_fund(str(object_result['address']), object_result['private_key'], "ce272fa66352afe673cf3da5f0a245f827ef4462bc3221b665d6cecf1d36f387", 0,  'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB', 1000)
    #     elif choice == '3':
    #         key1 = b'\x0fy\x1c\x05\xa7\xc0\x05"\xd5E\xa2\xc2\xa4g\xd7\xae\x15\xc4\xb2\x02\x9at\xdfU\xee\xbd\x8b\xeaT\x8d\xf2\xbf'
    #         key2 = b'\x05tc\xd9\xa3\xa0\x8cd\xcfT\x1f\x15\r\x975yu\xdf\xcfW:\x19o\x15s\x16\x9f\x1dW,GB'
    #         address = wallet.address.create_addr_P2SH([key1, key2])
    #         print("Redeem Script:", address['redeem_script'])
    #         print("Multisig Address:", address['multisig_address'])
    #     elif choice == '4':
    #         key1 = b'\x0fy\x1c\x05\xa7\xc0\x05"\xd5E\xa2\xc2\xa4g\xd7\xae\x15\xc4\xb2\x02\x9at\xdfU\xee\xbd\x8b\xeaT\x8d\xf2\xbf'
    #         key2 = b'\x05tc\xd9\xa3\xa0\x8cd\xcfT\x1f\x15\r\x975yu\xdf\xcfW:\x19o\x15s\x16\x9f\x1dW,GB'
    #         wallet.spend_locked_fund_multisig_address([key1, key2], 'f201adbf9854722aea9ca6b95457f662c04ff7d4e997eb1b783387fbde2078eb', 0, 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB', 1000)
    #     elif choice == '5':
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")
