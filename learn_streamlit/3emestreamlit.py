import streamlit as st

if "text_list" not in st.session_state:
    st.session_state.text_list=[]

user_input=st.text_input("Enter some Text:")

if st.button("Append"):
    st.session_state.text_list.append(user_input)
if st.button("Clear"):
    st.session_state.text_list=[]

st.write("Text:", st.session_state.text_list)