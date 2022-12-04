import streamlit as st
from PIL import Image

st.text('Jeep')
st.image('https://techcrunch.com/wp-content/uploads/2022/09/JP023_279WR5jvo53mde21dbrr902p5rahl1e.jpg')
st.text_input('Your purchasing address')
st.text('50,000')
btn = st.button('Confirm')