import streamlit as st
from verification import verify_payment
import time
import webbrowser

price = '50,000'
st.text('Jeep')
st.image('https://techcrunch.com/wp-content/uploads/2022/09/JP023_279WR5jvo53mde21dbrr902p5rahl1e.jpg')
addy = st.text_input('Enter your purchasing address to confirm transaction')
email = st.text_input('How should we contact you?')
st.text(price)
btn = st.button('Confirm')
if btn:
    cost = int(price.replace(',', ''))
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