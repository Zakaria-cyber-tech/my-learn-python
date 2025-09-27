import json
import os
import streamlit as st
import pandas as pd
from datetime import datetime

USERS_FILE = "users.json"
LOGS_FILE = "logs.json"

# ================= Helpers =================
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def load_logs():
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_logs(logs):
    with open(LOGS_FILE, "w") as f:
        json.dump(logs, f, indent=4)

def add_log(user, action, amount, target=None):
    logs = load_logs()
    logs.append({
        "user": user,
        "action": action,
        "amount": amount,
        "target": target,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_logs(logs)

# ================= Logic =================
def register(username, password):
    users = load_users()
    if username in users:
        return False, "⚠️ Username already exists!"
    users[username] = {"password": password, "money": 0}
    save_users(users)
    return True, "✅ Registration successful!"

def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        return True, users[username]["money"]
    return False, "❌ Invalid username or password."

def delete_account(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        del users[username]
        save_users(users)
        return True, "🗑️ Account deleted successfully!"
    return False, "⚠️ Invalid username or password."

def save_current_money(username, money):
    users = load_users()
    if username in users:
        users[username]["money"] = money
        save_users(users)

def transfer_money(sender, receiver, amount):
    users = load_users()
    if sender not in users or receiver not in users:
        return False, "⚠️ User not found!"
    if users[sender]["money"] < amount:
        return False, "⚠️ Not enough balance!"
    users[sender]["money"] -= amount
    users[receiver]["money"] += amount
    save_users(users)
    add_log(sender, "Transfer", -amount, target=receiver)
    add_log(receiver, "Received", amount, target=sender)
    return True, f"✅ Transferred {amount}$ to {receiver}"

# ================= Streamlit UI =================
st.set_page_config(page_title="Bank App", page_icon="💰")

if "user" not in st.session_state:
    st.session_state.user = None
if "money" not in st.session_state:
    st.session_state.money = 0

st.title("🏦 Mini Bank App")

# --------- If user not logged in ----------
if st.session_state.user is None:
    tab1, tab2, tab3 = st.tabs(["🔑 Login", "📝 Register", "❌ Delete Account"])

    with tab1:
        username = st.text_input("Username (Login)")
        password = st.text_input("Password (Login)", type="password")
        if st.button("Login"):
            ok, res = login(username, password)
            if ok:
                st.session_state.user = username
                st.session_state.money = res
                st.success("✅ Login successful!")
            else:
                st.error(res)

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Register"):
            ok, res = register(new_user, new_pass)
            if ok:
                st.success(res)
            else:
                st.error(res)

    with tab3:
        del_user = st.text_input("Username (Delete)")
        del_pass = st.text_input("Password (Delete)", type="password")
        if st.button("Delete Account"):
            ok, res = delete_account(del_user, del_pass)
            if ok:
                st.success(res)
            else:
                st.error(res)

# --------- If user logged in ----------
else:
    st.subheader(f"🔥 Current user: {st.session_state.user}")
    st.metric("💰 Balance", f"{st.session_state.money} $")

    tab1, tab2, tab3, tab4 = st.tabs(["💵 Actions", "📜 Transactions", "🔄 Transfer", "🚪 Logout"])

    # Deposit / Withdraw
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            deposit = st.number_input("Deposit amount", min_value=0.0, step=1.0)
            if st.button("Deposit"):
                st.session_state.money += deposit
                save_current_money(st.session_state.user, st.session_state.money)
                add_log(st.session_state.user, "Deposit", deposit)
                st.success(f"✅ Deposited {deposit}$")

        with col2:
            withdraw = st.number_input("Withdraw amount", min_value=0.0, step=1.0)
            if st.button("Withdraw"):
                if withdraw <= st.session_state.money:
                    st.session_state.money -= withdraw
                    save_current_money(st.session_state.user, st.session_state.money)
                    add_log(st.session_state.user, "Withdraw", -withdraw)
                    st.success(f"✅ Withdrew {withdraw}$")
                else:
                    st.error("⚠️ Not enough balance.")

    # Transactions log
    with tab2:
        logs = load_logs()
        user_logs = [log for log in logs if log["user"] == st.session_state.user or log.get("target") == st.session_state.user]
        if user_logs:
            df = pd.DataFrame(user_logs)
            st.dataframe(df)
        else:
            st.info("No transactions yet.")

    # Transfer money
    with tab3:
        users = load_users()
        all_users = list(users.keys())
        receiver = st.selectbox("Choose receiver", [u for u in all_users if u != st.session_state.user])
        amount = st.number_input("Amount to transfer", min_value=0.0, step=1.0)
        if st.button("Transfer"):
            ok, res = transfer_money(st.session_state.user, receiver, amount)
            if ok:
                st.session_state.money -= amount
                st.success(res)
            else:
                st.error(res)

    # Logout
    with tab4:
        if st.button("Logout"):
            save_current_money(st.session_state.user, st.session_state.money)
            st.session_state.user = None
            st.session_state.money = 0
            st.info("Logged out successfully.")
