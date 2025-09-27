import streamlit as st
import pandas as pd

@st.cache_data
def load_file(filer):
    return pd.read_csv(filer)

st.sidebar.title("List")

with st.sidebar:
    st.header("وسير تقرى")

tab1, tab2, tab3=st.tabs(["Upload", "Show", "chat"])

with tab1:
    filer=st.file_uploader("Upload Your File:", type=("csv"))

with tab2:
    if filer is not None:
        df=load_file(filer)
        n_rows=st.slider("Choose The number Of Rows", max_value=len(df), min_value=1)
        lt=st.multiselect("choose", df.columns, default=df.columns)
        st.write(df[:n_rows][lt])

with tab3:
    col1, col2, col3=st.columns(3)
with col1:
    st.text_input("Enter The Text")
    st.write("هاذه النافذة غير مهمة")
