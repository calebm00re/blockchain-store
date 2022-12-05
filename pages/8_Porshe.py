import streamlit as st
from verification import verify_payment

price = '260,000'
st.text('Porshe')
st.image('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/1804-jlgt3rs-0003-jpg-1524759932.jpg')
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