from urllib.request import urlopen
from helper import decode_base58, SIGHASH_ALL, hash256, little_endian_to_int
from script import p2pkh_script, Script 
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey
from secrets import Secrets
import json


def verify_payment(amount=None, addy=None):
    # Getting the block history
    data = urlopen('https://api.blockcypher.com/v1/btc/test3/addrs/mnMCmnP16B6uK2VeCrAEFwpwEHKpNhxcLT/full?limit=50')
    total = ''
    # Making the block history more useful
    for line in data.readlines():
        total += line.decode("utf-8")
    j = json.loads(total)

    to_check = None
    # print(j['txs'])
    for tx in j['txs']:
        for ad in tx['addresses']:
            if ad == addy:
                to_check = tx
                break
        # print(tx['addresses'])
    print(to_check)
    return

verify_payment(addy='mrgVZ8BxXChc2xjXzX25ViYsppLfLoBfC1')