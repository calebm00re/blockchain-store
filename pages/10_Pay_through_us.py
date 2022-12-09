import streamlit as st
from verification import make_tx, blacklist_tx
from prices import prices
import time
from blockcypher import pushtx


new_title = '<p style="font-family:sans-serif; font-size: 42px;">Complete Your Purchase With Us!</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.text('We use your client-side processing')
st.text('Ensuring we never have access to any of your secure information')
st.text('This will create a 1 input 2 outout transaction')
st.text(' ')
st.text(' ')
st.text(' ')

ps = st.text_input('Wallet Passphrase')
addy = st.text_input('Your wallet')
prev_tx = st.text_input('Previous Transaction')
prev_index = st.text_input('Previous Index')
change = st.text_input('Change you want returned to your wallet')
contact_type = None

contact_type = st.selectbox('How would you like to arrange delivery', ('select', 'Email', 'Phone'))
contact = st.text_input('Contact' if contact_type == 'select' else contact_type)

choice = st.selectbox('Product',
    ('select', 'Jeep', 'Silverado', 'GR86', 'G63', 'Camaro', 'Cadillac', 'Hummer', 'Porsche', 'Challenger'))

st.text(' ')
st.text(' ')
if choice != 'select':
    st.text(prices[choice])

btn = st.button('Confirm')

if btn:
    if contact_type == 'select' or choice == 'select' or contact == '' or ps == '':
        st.error('Please complete the form', icon='🛑')
    else:
        cost = prices[choice].replace(',', '')
        st.text(cost)
        tx = make_tx(cost, change, prev_tx, ps, int(prev_index), addy)
        res = pushtx(tx_hex=tx['val'], coin_symbol='btc-testnet',api_key='88e698204c374ec4b06c8edc4b6f45e2')
        if 'error' in res.keys():
            st.error('Something went wrong, please try again', icon='🛑')
        else:
            with st.spinner('Creating Transaction'):
                time.sleep(5)
            blacklist_tx(res['tx']['hash'], contact, choice)
            st.success('Purchase Successful, we will reach out soon', icon="✅")
            st.balloons()