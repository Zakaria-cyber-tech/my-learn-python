import streamlit as st

if "activator" not in st.session_state:
    st.session_state.activator=""

st.sidebar.title("تحديث قادم...")


if st.session_state.activator=="active" or st.session_state.activator=="admin":
    if "text_list" not in st.session_state:
        st.session_state.text_list=[]

    user_input=st.text_input("Enter some Text:")

    if st.button("Append"):
        st.session_state.text_list.append(user_input)
    if st.button("Clear"):
        st.session_state.text_list=[]

    st.write("Text:", st.session_state.text_list)
else:
    st.title("ليس مهم")
    st.warning("⚠️ Please log in from the main page")