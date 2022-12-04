import streamlit as st
from PIL import Image

st.text('G63')
st.image('https://media.gq-magazine.co.uk/photos/5d13aeaf976fa3a41af3b3f7/master/pass/mercedes-02-gq-12nov18_b.jpg')
st.text_input('Your purchasing address')
st.text('50,000')
btn = st.button('Confirm')