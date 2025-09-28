import streamlit as st

if "activator" not in st.session_state:
    sess=st.session_state.activator=""

st.set_page_config(page_title="WELCOM")

st.sidebar.success("Choose The Tabs...")

st.write("# Welcome To My site:")


user=st.text_input("Enter You name(The log in for just admins)").lower()
password=st.text_input("The Password(''')").lower()
bt=st.button("Sign in")
if bt:
    if user=="zakaria" and password=="zakaria":
        sess="active"
        st.success("✔️​sign in is successfully")
        st.info("Click The arrow To open sidebar")
    else:
        st.error("❌​​The user or password is not ivable")
