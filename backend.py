from urllib.request import urlopen
from helper import decode_base58, SIGHASH_ALL, hash256, little_endian_to_int
from script import p2pkh_script, Script 
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey
from secrets import Secrets
import json


def get_transaction_hex(price=None, gas=None, target_addy=None, change_addy=None):
    s = Secrets()
    store_addy = str(s.get_address())
    url = 'https://api.blockcypher.com/v1/btc/test3/addrs/' + store_addy + '/full?limit=50'
    data = urlopen(url)
    total = ''
    for line in data.readlines():
        total += line.decode("utf-8")
        # print(line.decode("utf-8"))
    # print(j)
    j = json.loads(total)
    print(j['txs'])
    return

get_transaction_hex()