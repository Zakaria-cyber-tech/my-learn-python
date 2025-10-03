import streamlit as st
import time as tm
class User:
    def __init__(self, user, password, idd):
        self.user=user
        self.password=password
        self.idd=idd
    def __str__(self):
        return f"{self.user}\n{self.password}\n{self.idd}"
    
st.title("Welcom To Tramway siteweb")
st.text_input("Enter Your User:")
st.text_input("Enter Your Password:")
if st.button("Log in"):
    pass