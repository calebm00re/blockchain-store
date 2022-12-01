from helper import decode_base58, SIGHASH_ALL, hash256, little_endian_to_int
from script import p2pkh_script, Script 
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey


def get_transaction_hex(price, gas, sender, recipient, item):
 
    prev_tx = bytes.fromhex('a2161ef314805a016b6587481aab4bac7754330ab59bb961d44b9468431ef88a') 
    prev_index = 0 
    
    target_address = 'mtjfgktYZdoEt8XgU5gM7BRx4yrHsqY1yG' 
    target_amount = 0.0002 
    change_address = 'mrgVZ8BxXChc2xjXzX25ViYsppLfLoBfC1' 
    change_amount = 0.0002 
    
    passphrase = b'celsius is crack' 
    secret = little_endian_to_int(hash256(passphrase)) 
    priv = PrivateKey(secret) 
    
    tx_ins = [] 
    tx_ins.append(TxIn(prev_tx, prev_index)) 
    
    tx_outs = [] 
    h160 = decode_base58(target_address) 
    
    script_pubkey = p2pkh_script(h160) 
    target_satoshis = int(target_amount*100000000) 
    tx_outs.append(TxOut(target_satoshis, script_pubkey)) 
    h160 = decode_base58(change_address) 
    script_pubkey = p2pkh_script(h160) 
    change_satoshis = int(change_amount*100000000) 
    tx_outs.append(TxOut(change_satoshis, script_pubkey)) 
    
    tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True) 
    
    print(tx_obj.sign_input(0, priv)) 
    
    print(tx_obj.serialize().hex())
    return