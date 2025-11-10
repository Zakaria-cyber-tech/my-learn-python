import streamlit as st
import time

if "activator" not in st.session_state:
    st.session_state.activator=""

st.sidebar.title("Configuration:")
with st.slidebar:
    stars=st.selectbox("قيم موقع زكرياء",["1/5","2/5","3/5","4/5","5/5"])

if st.session_state.activator="active" or st.session_state.activator="admin":
    with st.sidebar:
        sel=st.selectbox("Choose The Type of calculate:", ["+", "-", "x", "/"])
        if stars=="1/5" or stars=="2/5":
            st.write("Thanks For Using My sitweb")
        elif stars=="3/5":
            st.write("**I LOVE YOU**")
        else:
            st.write("OOOOOOOOh Thanks")
    

st.header("Speed Calculater")
with st.spinner("Loading..."):
    
    if st.session_state.activator=="active" or st.session_state.activator=="admin":
            if sel=="+":
                st.write("Let's To +")
                first=st.number_input("Enter The First Number:", min_value=0, max_value=999999999999,step=1)
                last=st.number_input("Enter The Last Number:", min_value=0, max_value=999999999999,step=1)
                btn=st.button("Press To Calcule")
                if btn:
                    result=first + last
                    st.header(result)
            elif sel=="-":
                st.write("Let's To -")
                first=st.number_input("Enter The First Number:", min_value=0, max_value=999999999999,step=1)
                last=st.number_input("Enter The Last Number:", min_value=0, max_value=999999999999,step=1)
                btn=st.button("Press To Calcule")
                if btn:
                    result=first - last
                    st.header(result)
            elif sel=="x":
                st.write("Let's To x")
                first=st.number_input("Enter The First Number:", min_value=0, max_value=999999999999,step=1)
                last=st.number_input("Enter The Last Number:", min_value=0, max_value=999999999999,step=1)
                btn=st.button("Press To Calcule")
                if btn:
                    result=first * last
                    st.header(result)
            elif sel=="/":
                st.write("Let's To /")
                first=st.number_input("Enter The First Number:", min_value=0, max_value=999999999999,step=1)
                last=st.number_input("Enter The Last Number:", min_value=0, max_value=999999999999,step=1)
                btn=st.button("Press To Calcule")
                if btn:
                    result=first / last
                    st.header(result)
    else:
        st.warning("⚠️ Please log in from the main page")
