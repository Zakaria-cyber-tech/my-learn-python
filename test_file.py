import streamlit as st
import pandas as pd

@st.cache_data
def load_file(file):
    return pd.read_xml(file)

file=st.file_uploader("Enter The File XML:", type="xml")

try:
    if file is not None:
        df=load_file(file)
        st.write(df)
except:
    st.write("Error In your file")