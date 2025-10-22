import streamlit as st
import pandas as pd

if "activator" not in st.session_state:
    st.session_state.activator=""

@st.cache_data
def read_txt(file):
    content=file.read().decode("utf-8")
    content=content.replace("\n","  \n")
    return content
@st.cache_data
def read_csv(file):
    content=pd.read_csv(file)
    return content
@st.cache_data
def read_excel(file):
    content=pd.read_excel(file)
    return content
@st.cache_data
def read_json(file):
    content=pd.read_json(file)
    return content

def read_image(file):
    return st.image(file)

tab1, tab2, tab3, tab4,tab5=st.tabs(["TXT","Exel","CSV","JSON","IMAGES"])
with tab1:
    try:
        file1=st.file_uploader("Upload TXT File:", type="txt")
        if file1 is not None:
            st.write(read_txt(file1))
    except:
        st.error("❌ Error load TXT")
with tab3:
    file2=st.file_uploader("Upload CSV File:", type="csv")
    if file2 is not None:
        try:
            lo=read_csv(file2)
            n_row=st.slider("Chos The number:", min_value=1, max_value=len(lo))
            st.write(lo[:n_row])
        except:
            st.error("❌ Error load image")
with tab2:
    try:
        file3=st.file_uploader("Upload excel File:", type="xlsx")
        if file3 is not None:
            st.write(read_excel(file3))
    except:
        st.error("❌ Error load exel file")
with tab4:
    try:
        file4=st.file_uploader("Upload json File:", type="json")
        if file4 is not None:
            st.write(read_json(file4))
    except:
        st.error("❌ Error load json File")
with tab5:
    try:
        file5=st.file_uploader("Upload image file:", type="png")
        if file5 is not None:
            read_image(file5)
    except:
        st.error("❌ Error load image")

    