import streamlit as st
from verification import verify_payment

price = '60,000'
st.text('Silverado')
st.image('https://www.motortrend.com/uploads/2022/01/2024-Chevrolet-Silverado-EV-Trail-Boss.jpg')
addy = st.text_input('Enter your purchasing address to confirm transaction')
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
    res = verify_payment(cost, addy)
    if res:
        st.success('Your purchase has been confirmed! Delivery arrangements will be made shortly!')
    else:
        st.warning('An error has occured. Consider trying again later or making sure your payment went through.')