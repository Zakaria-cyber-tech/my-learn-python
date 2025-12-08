import streamlit as st
import json
import os
import time

st.set_page_config(page_title="WELCOME To Zakaeia siteweb")

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "user_list.json"))



def load_users():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    except Exception as e:
        st.error(f"Error loading users file: {e}")
        return {}

def save_users(users):
    try:
        parent = os.path.dirname(DATA_FILE)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        st.error(f"Failed to save users file: {e}")
        return False

users = load_users()

if "activator" not in st.session_state:
    st.session_state.activator = ""

#start
with st.spinner("Looding..."):
    placeholder = st.empty()
    with placeholder.container():
        st.sidebar.success("Choose The Tabs...")

        st.write("# Welcome To My site:")
        
        if st.session_state.activator != "active" and st.session_state.activator != "admin":
            tab1, tab2 = st.tabs(["Sign in", "New account"])
            with tab1:
                user = st.text_input("Enter your name")
                password = st.text_input("Password", type="password")
                if st.button("Sign in🔑"):
                    if user=="admin" and password=="admin":
                        st.session_state.activator = "admin"
                        st.success("✔️ Welecom Admin You are the best")
                    elif user in users and users[user].get("password") == password:
                        st.session_state.activator = "active"
                        st.success("✔️ Sign in successful")
                        st.info("Click the arrow to open sidebar")
                        time.sleep(3)
                        st.rerun()
                    else:
                        st.error("❌ The username or password is invalid")
            with tab2:
                new_user = st.text_input("New username", key="new_user")
                new_password = st.text_input("New password", type="password", key="new_password")
                if st.button("Create account"):
                    if new_user=="admin" or new_password=="admin":
                        st.error("❌This User is usag with admin(pleas Try another user)")
                    elif not new_user:
                        st.error("Please enter a username")
                    elif new_user in users:
                        st.error("User already exists")
                    else:
                        users[new_user] = {"password": new_password}
                        if save_users(users):
                            st.success("Account created successfully")
        elif st.session_state.activator=="active":
            tab11, tab22=st.tabs(["Main", "delet user"])
            with tab11:
                if st.button("Reflesh"):
                    st.rerun()
                st.warning("⚠️ Please go to Pages...")
                if st.button("sign out"):
                    st.session_state.activator=""
                    st.rerun()
            with tab22:
                user_del=st.text_input("Enter your user To verify:")
                user_pass_del=st.text_input("Enter your password")
                if st.button("Ok."):
                    if user_del in users and users[user_del].get("password")==user_pass_del:
                        del users[user_del]
                        if save_users(users):
                            st.success("✅ Del success, after 2sec you are sign out.")
                            st.session_state.activator=""
                            time.sleep(2)
                            st.rerun()
                    else:
                        st.error("⚠️ This user is not found,check your information")
    if st.session_state.activator=="admin":
        time.sleep(2)
        placeholder.empty()
        st.title("Hi Admin")
        if st.button("reflesh"):
            st.rerun()
        if st.button("sign out"):
            st.session_state.activator=""
            st.rerun()
        st.subheader("🗑️ Delete a user")
        del_user = st.text_input("Enter username to delete:")

        if st.button("Delete user"):
            if del_user in users:
                del users[del_user]
                if save_users(users):
                    st.success(f"✅ User '{del_user}' deleted successfully.")
                    st.rerun()
                else:
                    st.error("❌ Error in save;pleas try again.")
            else:
                st.error("❌ User not found.")
        st.write(users)

