import streamlit as st
from verification import verify_payment

price = '70,000'
st.text('Camaro')
st.image('https://media.chevrolet.com/content/dam/Media/images/US/Vehicles/Chevrolet/Cars/Camaro_ZL1/2018/Product/2018-Chevrolet-Camaro-ZL1-1LE-001.jpg')
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