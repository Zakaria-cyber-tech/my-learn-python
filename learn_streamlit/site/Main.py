import streamlit as st
import json
import os
import time

st.set_page_config(page_title="WELCOME")

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "user_list.json"))

admin_users=[]
try:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            admin_users=json.load(f)
except Exception as e:
    st.error(f"Error loading users file: {e}")


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

placeholder = st.empty()
with placeholder.container():
    st.sidebar.success("Choose The Tabs...")

    st.write("# Welcome To My site:")

    tab1, tab2 = st.tabs(["Sign in", "New account"])

    if st.session_state.activator != "active" and st.session_state.activator != "admin":
        with tab1:
            user = st.text_input("Enter your name")
            password = st.text_input("Password", type="password")
            if st.button("Sign in"):
                if user=="admin" and password=="admin":
                    st.session_state.activator = "admin"
                    st.success("✔️ Welecom Admin You are the best")
                elif user in users and users[user].get("password") == password:
                    st.session_state.activator = "active"
                    st.success("✔️ Sign in successful")
                    st.info("Click the arrow to open sidebar")
                else:
                    st.error("❌ The username or password is invalid")

        with tab2:
            new_user = st.text_input("New username", key="new_user")
            new_password = st.text_input("New password", type="password", key="new_password")
            if st.button("Create account"):
                if new_user=="admin":
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
        st.warning("⚠️ Please go to Pages...")
if st.session_state.activator=="admin":
    time.sleep(2)
    placeholder.empty()
    st.title("Hi Admin")
    st.write(admin_users)

