from urllib.request import urlopen
from helper import decode_base58, SIGHASH_ALL, hash256, little_endian_to_int
from script import p2pkh_script, Script 
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey
from secrets import Secrets
import json


def get_transaction_hex(price, gas, prev_idx, prev_tx, change_addy=None):
    prev_tx = bytes.fromhex(prev_tx)
    secrets = Secrets()

    if change_addy is None:
        change_addy = secrets.get_address()

    tx_ins = []
    tx_ins.append(TxIn(prev_tx, prev_idx))

    tx_outs = []
    h160 = decode_base58(secrets.get_address())

    script_pubkey = p2pkh_script(h160)
    target_satoshis = int(price*100000000)
    tx_outs.append(TxOut(target_satoshis, script_pubkey))
    h160 = decode_base58(change_addy)
    script_pubkey = p2pkh_script(h160)
    change_satoshis = int((price-gas)*100000000)
    tx_outs.append(TxOut(change_satoshis, script_pubkey))

    tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True)

    print(tx_obj.sign_input(0, secrets.get_priv()))

    print(tx_obj.serialize().hex())
    return

get_transaction_hex(.0003, .0001, 1, 'c184a5551747beda8f676f84dd6e91da550482e9fd18e65f95a9b5fb399f18b2')