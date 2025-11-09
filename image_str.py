import streamlit as st
from PIL import Image

img = Image.open("C:\\Users\\Zaka-PC\\Desktop\\sora.png")

st.image(img, caption="# hi evryon", use_container_width=True)
