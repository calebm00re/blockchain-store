import streamlit as st
from verification import verify_payment
import time

price = '60,000'
st.text('Silverado')
st.image('https://www.motortrend.com/uploads/2022/01/2024-Chevrolet-Silverado-EV-Trail-Boss.jpg')
addy = st.text_input('Enter your purchasing address to confirm transaction')
contact_type = st.selectbox('How would you like to arrange delivery', ('select', 'Email', 'Phone'))
contact = st.text_input('Contact' if contact_type == 'select' else contact_type)
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
    if addy != '' and contact_type != 'select' and contact != '':
        res = verify_payment(cost, addy, contact)
        with st.spinner('Scanning our store wallet...'):
            time.sleep(3)
        if res['result']:
            st.balloons()
            st.success(res['reason'], icon="✅")
        else:
            if res['severity'] == 1:
                st.warning(res['reason'], icon='⚠️')
            else:
                st.error(res['reason'], icon='🛑')
    else:
        st.error('Please complete the form', icon='🛑')