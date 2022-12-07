import streamlit as st
from verification import verify_payment
import time

price = '80,000'
st.text('Escalade')
st.image('https://static.foxbusiness.com/foxbusiness.com/content/uploads/2022/10/escalade.jpg')
addy = st.text_input('Enter your purchasing address to confirm transaction')
contact_type = st.selectbox('How would you like to arrange delivery', ('select', 'Email', 'Phone'))
contact = st.text_input('Contact' if contact_type == 'select' else contact_type)
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
    if addy != '' and contact_type != 'select' and contact != '':
        res = verify_payment(cost, addy)
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