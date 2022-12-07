from urllib.request import urlopen
import json
from ecc import PrivateKey
from helper import decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from helper import hash256, little_endian_to_int

def blacklist_tx(used_hash):
    f = open("history.txt", "a")
    f.write(used_hash)
    f.write('\n')
    f.close()
    return

def check_blacklist(possible_hash):
    f = open("history.txt", 'r')
    for line in f.readlines():
        if possible_hash == line.strip():
            return False
    return True

def verify_payment(amount, addy, ):
    # Getting the block history
    data = urlopen('https://api.blockcypher.com/v1/btc/test3/addrs/mnMCmnP16B6uK2VeCrAEFwpwEHKpNhxcLT/full?limit=50')
    total = ''
    # Making the block history more useful
    for line in data.readlines():
        total += line.decode("utf-8")
    j = json.loads(total)

    to_check = None
    for tx in j['txs']:
        for ad in tx['addresses']:
            if ad == addy:
                to_check = tx
                break

    # Ensure total, single-spend, and confirmations
    if to_check is None:
        return {
                    'result': False,
                    'reason': 'Please check the address you\'ve entered.',
                    'severity': 1
                }
    response = check_blacklist(to_check['hash'])
    if not response:
        return {
                    'result': False,
                    'reason': 'This transaction has already been verified',
                    'severity': 1
                }
    response = response and (to_check['total'] - to_check['fees']) > amount
    if not response:
        return {
                    'result': False,
                    'reason': 'Funds too low, please contact staff.',
                    'severity': 2
                }
    response = response and not (to_check['double_spend'])
    if not response:
        return {
                    'result': False,
                    'reason': 'Double spend.',
                    'severity': 2
                }
    response = response and (to_check['confirmations'] >= 6)
    if not response:
        return {
                    'result': False,
                    'reason': 'Confirmations too low, please try again later.',
                    'severity': 1
                }

    if response:
        blacklist_tx(to_check['hash'])
    
    return {
                'result': True,
                'reason': 'Your purchase has been confirmed! We will reach out for delivery arrangements!',
                'severity': 0
            }

def make_tx(price, change, prev_tx, passphrase, prev_index, address):
    prev_tx = bytes.fromhex(prev_tx)

    store_addy = 'mnMCmnP16B6uK2VeCrAEFwpwEHKpNhxcLT'

    passphrase = str.encode(passphrase)
    secret = little_endian_to_int(hash256(passphrase))
    priv = PrivateKey(secret)

    tx_ins = []
    tx_ins.append(TxIn(prev_tx, prev_index))

    tx_outs = []
    h160 = decode_base58(store_addy)

    script_pubkey = p2pkh_script(h160)
    target_satoshis = int(price)
    tx_outs.append(TxOut(target_satoshis, script_pubkey))
    h160 = decode_base58(address)
    script_pubkey = p2pkh_script(h160)
    change_satoshis = int(change)
    tx_outs.append(TxOut(change_satoshis, script_pubkey))

    tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True)
    # print(tx_obj.sign_input(0, priv))
    # print(tx_obj.serialize().hex())
    return {'res': tx_obj.sign_input(0, priv), 'val': tx_obj.serialize().hex()}