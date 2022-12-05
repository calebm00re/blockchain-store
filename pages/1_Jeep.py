import streamlit as st
from verification import verify_payment

price = '50,000'
st.text('Jeep')
st.image('https://techcrunch.com/wp-content/uploads/2022/09/JP023_279WR5jvo53mde21dbrr902p5rahl1e.jpg')
addy = st.text_input('Enter your purchasing address to confirm transaction')
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
    st.text(verify_payment(cost, addy))