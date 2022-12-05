import streamlit as st
from verification import verify_payment

price = '80,000'
st.text('Escalade')
st.image('https://static.foxbusiness.com/foxbusiness.com/content/uploads/2022/10/escalade.jpg')
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