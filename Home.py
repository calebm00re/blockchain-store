from urllib.request import urlopen
from helper import decode_base58, SIGHASH_ALL, hash256, little_endian_to_int
from script import p2pkh_script, Script 
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey
# from secrets import Secrets
import json
import streamlit as st
from PIL import Image
from st_clickable_images import clickable_images
import webbrowser
import streamlit.components.v1 as components
from bokeh.models.widgets import Div

st.set_page_config(page_icon='🛻', initial_sidebar_state='expanded', layout='wide')

new_title = '<p style="font-family:sans-serif; font-size: 42px;">Welcome to Caleb and Blake\'s Auto Store!</p>'
st.markdown(new_title, unsafe_allow_html=True)

# st.markdown('<p class="big-font">Welcome to Caleb and Blake\'s Auto Store!</p>', unsafe_allow_html=True)
# st.text('Welcome to Caleb and Blake\'s Auto Store')
clicked = clickable_images(
    [
        "https://techcrunch.com/wp-content/uploads/2022/09/JP023_279WR5jvo53mde21dbrr902p5rahl1e.jpg",
        "https://www.motortrend.com/uploads/2022/01/2024-Chevrolet-Silverado-EV-Trail-Boss.jpg",
        "https://i.ibb.co/j5BDZWJ/yoda.png",
        "https://media.gq-magazine.co.uk/photos/5d13aeaf976fa3a41af3b3f7/master/pass/mercedes-02-gq-12nov18_b.jpg"
    ],
    titles=[f"Image #{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "2rem", "height": "10rem"},
)

if clicked == 1:
    btn = st.button('Go to truck')
    if btn:
        js = "window.location.href = 'http://localhost:8501/Silverado'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

# image = Image.open('sunrise.jpg')

# st.image(image, caption='Sunrise by the mountains')

# class shopping_card:
#     def __init__(self, name, img, img_cap, price):
#         self.name = name
#         self.img = img
#         self.img_cap = img_cap
#         self.price = price
#         self.btn_text = 'Buy'
#     def show_card(self):
#         st.text(self.name)
#         st.image(Image.open(self.img))
#         st.text_input('Your purchasing address')
#         st.text(self.price)
#         btn = st.button(self.btn_text)


# def blacklist_tx(used_hash):
#     f = open("history.txt", "a")
#     f.write(used_hash)
#     f.write('\n')
#     f.close()
#     return

# def check_blacklist(possible_hash):
#     f = open("history.txt", 'r')
#     for line in f.readlines():
#         if possible_hash == line.strip():
#             return False
#     return True

# def verify_payment(amount, addy):
#     # Getting the block history
#     data = urlopen('https://api.blockcypher.com/v1/btc/test3/addrs/mnMCmnP16B6uK2VeCrAEFwpwEHKpNhxcLT/full?limit=50')
#     total = ''
#     # Making the block history more useful
#     for line in data.readlines():
#         total += line.decode("utf-8")
#     j = json.loads(total)

#     to_check = None
#     for tx in j['txs']:
#         for ad in tx['addresses']:
#             if ad == addy:
#                 to_check = tx
#                 break

#     # Ensure total, single-spend, and confirmations
#     response = (to_check['total'] - to_check['fees']) > amount
#     response = response and not (to_check['double_spend'])
#     response = response and (to_check['confirmations'] >= 6)
#     response = response and check_blacklist(to_check['hash'])

#     if response:
#         blacklist_tx(to_check['hash'])

#     return response

# res = (verify_payment(50, 'mrgVZ8BxXChc2xjXzX25ViYsppLfLoBfC1'))
# print(res)
# sc = shopping_card('Jeep', 'jeep.png', 'jeep', '50,000')
# sc.show_card()
# co.execute("""INSERT INTO example VALUES(?)""", (comment,))
