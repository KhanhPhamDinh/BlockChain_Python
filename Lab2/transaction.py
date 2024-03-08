import string
from binascii import unhexlify

from Crypto.Util import number
from bitcoin.core import CMutableTxIn, CMutableTxOut, CMutableTransaction, b2x, lx, COutPoint, Hash160
from bitcoin.wallet import P2PKHBitcoinAddress, CBitcoinSecret
from bitcoin.core.script import CScript, OP_CHECKSIG, SignatureHash, SIGHASH_ALL, OP_HASH160, OP_DUP, OP_EQUALVERIFY
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH


def create_txin(txid: string, output_index: number):
    # Create a transaction input (TxIn)
    txin = CMutableTxIn(COutPoint(lx(txid), output_index))
    return txin


def create_txout(amount_to_send: int, destination_address: string):
    # Create a transaction output (TxOut) to the desired destination address
    txout = CMutableTxOut(amount_to_send, P2PKHBitcoinAddress(destination_address).to_scriptPubKey())
    return txout


def create_signed_transaction_p2pkh(txin: CMutableTxIn, txout: CMutableTxOut, private_key: CBitcoinSecret):
    # Create the unsigned transaction
    tx = CMutableTransaction([txin], [txout])
    txin_scriptPubKey = CScript([OP_DUP, OP_HASH160, Hash160(private_key.pub), OP_EQUALVERIFY, OP_CHECKSIG])

    # Sign the transaction
    # Compute the signature hash for the input
    sighash = SignatureHash(txin_scriptPubKey, tx, 0, SIGHASH_ALL)
    # Sign the hash with the private key
    signature = private_key.sign(sighash) + bytes([SIGHASH_ALL])
    # Set the scriptSig of the transaction input
    txin.scriptSig = CScript([signature, private_key.pub])
    VerifyScript(txin.scriptSig, txin_scriptPubKey, tx, 0, (SCRIPT_VERIFY_P2SH,))

    return tx

def create_signed_transaction_p2sh(txin: CMutableTxIn, txout: CMutableTxOut, keys: list, redeem_script: CScript):

    # Create the unsigned transaction
    tx = CMutableTransaction([txin], [txout], nVersion=2)
    for key in keys:
        private_key = CBitcoinSecret.from_secret_bytes(key)
        txin_redeemScript = CScript([private_key.pub, OP_CHECKSIG])
        sighash = SignatureHash(txin_redeemScript, tx, 0, SIGHASH_ALL)
        signature = private_key.sign(sighash) + bytes([SIGHASH_ALL])
        txin.scriptSig = CScript([signature, txin_redeemScript])
        VerifyScript(txin.scriptSig, txin_redeemScript.to_p2sh_scriptPubKey(), tx, 0, (SCRIPT_VERIFY_P2SH,))

    # Now, the transaction tx is a signed transaction
    print("Signed Transaction:", tx)
    print("Signed Transaction hex:", b2x(tx.serialize()))
    return tx
