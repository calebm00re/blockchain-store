import streamlit as st
from PIL import Image

st.text('Silverado')
st.image('https://www.motortrend.com/uploads/2022/01/2024-Chevrolet-Silverado-EV-Trail-Boss.jpg')
st.text_input('Your purchasing address')
st.text('50,000')
btn = st.button('Confirm')