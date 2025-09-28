import streamlit as st
from PIL import Image

# تحميل الصورة
img = Image.open("C:\\Users\\Zaka-PC\\Desktop\\sora.png")

# عرض الصورة
st.image(img, caption="# hi evryon", use_container_width=True)
