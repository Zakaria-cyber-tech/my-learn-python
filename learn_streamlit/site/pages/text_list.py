import streamlit as st

if "activator" not in st.session_state:
    st.session_state.activator=""

st.sidebar.title("واش مكتفهمش قلت لك سير تقرى")

st.title("غير تخربيقة جاتني سخن عليا مخي")

if st.session_state.activator=="active":
    if "text_list" not in st.session_state:
        st.session_state.text_list=[]

    user_input=st.text_input("Enter some Text:")

    if st.button("Append"):
        st.session_state.text_list.append(user_input)
    if st.button("Clear"):
        st.session_state.text_list=[]

    st.write("Text:", st.session_state.text_list)
else:
    st.warning("⚠️ Please log in from the main page")