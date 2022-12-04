from urllib.request import urlopen
import json

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

def verify_payment(amount, addy):
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
    response = (to_check['total'] - to_check['fees']) > amount
    response = response and not (to_check['double_spend'])
    response = response and (to_check['confirmations'] >= 6)
    response = response and check_blacklist(to_check['hash'])

    if response:
        blacklist_tx(to_check['hash'])

    return response