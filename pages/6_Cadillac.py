import streamlit as st
from verification import verify_payment

price = '80,000'
st.text('Escalade')
st.image('https://static.foxbusiness.com/foxbusiness.com/content/uploads/2022/10/escalade.jpg')
addy = st.text_input('Your purchasing address')
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
    st.text(verify_payment(price, addy))
