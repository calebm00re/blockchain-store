import streamlit as st
from verification import verify_payment

price = '90,000'
st.text('G63')
st.image('https://media.gq-magazine.co.uk/photos/5d13aeaf976fa3a41af3b3f7/master/pass/mercedes-02-gq-12nov18_b.jpg')
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