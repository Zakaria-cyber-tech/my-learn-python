import json
import os
import time

def clear():
    os.system('cls' if os.name=="nt" else "clear")

USERS_FILE = "users.json"
bank_user = None      
user_log = None      
current_money = 0     


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


def register():
    users = load_users()
    username = input("Enter username: ").strip()
    if username in users:
        print("⚠️ Username already exists!")
        return None

    password = input("Enter password: ").strip()
    users[username] = {
        "password": password,
        "money": 0      
    }
    save_users(users)
    print("✅ Registration successful!")
    return username


def login():
    users = load_users()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        print("✅ Login successful!")
        return username
    else:
        print("❌ Invalid username or password.")
        return None


def delete_account():
    users = load_users()
    username = input("Enter username to delete: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        confirm = input("Are you sure you want to delete this account? (yes/no): ").lower()
        if confirm == "yes":
            del users[username]
            save_users(users)
            print("🗑️ Account deleted successfully!")
            return username
        else:
            print("❌ Deletion canceled.")
    else:
        print("⚠️ Invalid username or password.")
    return None


def start():
    global bank_user, user_log, current_money
    print("1) Register new account")
    print("2) Login")
    print("3) Delete account")
    print("4) Exit.")
    choice = input("👉 Choose an option: ")

    if choice == "1":
        bank_user = register()
        if bank_user:
            current_money = 0
            user_log = "active"
    elif choice == "2":
        bank_user = login()
        if bank_user:
            user_log = "active"
            users = load_users()
            current_money = users[bank_user]["money"] 
    elif choice == "3":
        deleted = delete_account()
        if deleted and bank_user == deleted:
            bank_user = None
            user_log = None
            current_money = 0
    elif choice=="4":
        clear()
        print("Ok...")
        time.sleep(2)
        exit()
    else:
        print("⚠️ Invalid option!")

    if bank_user:
        print(f"🔥 Current user: {bank_user}")
        
    else:
        print("🚪 No user logged in.")

    print(f"📌 user_log = {user_log}")


def save_current_money():
    global bank_user, current_money
    if bank_user:
        users = load_users()
        users[bank_user]["money"] = current_money
        save_users(users)
        print(f"💾 Saved money for {bank_user}: {current_money}")
    else:
        print("⚠️ No user logged in to save money.")

clear()
print(f"{'='*10} Welcome to Bank {'='*10}")
start()
clear()
while True:
    clear()
    if user_log == "active":
        print(f"💰 Current money: {current_money}")
        action = input("Do you want to (d)eposit, (w)ithdraw, (s)ave money, or (l)ogout? ").lower()
        if action == "d":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                current_money += amount
                print(f"✅ Deposited {amount}. New balance: {current_money}")
                save_current_money()
            else:
                print("⚠️ Invalid amount.")
        elif action == "w":
            try:
                amount = float(input("Enter amount to withdraw: "))
            except:
                pass
            try:
                if 0 < amount <= current_money:
                    current_money -= amount
                    print(f"✅ Withdrew {amount}. New balance: {current_money}")
                    save_current_money()
                else:
                    print("⚠️ invalid incorrect.")
            except:
                print("⚠️ Invalid amount.")
        elif action == "s":
            save_current_money()
        elif action == "l":
            save_current_money()
            bank_user = None
            user_log = None
            current_money = 0
            print("🚪 Logged out successfully.")
        else:
            print("⚠️ Invalid action.")
    else:
        start()
    time.sleep(2)
    clear()
    










