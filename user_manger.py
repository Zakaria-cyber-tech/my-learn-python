import json
import os

USERS_FILE = "users.json"
bank_user = None      # current logged in user
user_log = None       # "active" if user logged in, None otherwise


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
    users[username] = {"password": password}
    save_users(users)
    print("✅ Registration successful!")
    return username  # only updates bank_user, not user_log


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
    global bank_user, user_log
    print("1) Register new account")
    print("2) Login")
    print("3) Delete account")
    choice = input("👉 Choose an option: ")

    if choice == "1":
        bank_user = register()
    elif choice == "2":
        bank_user = login()
        if bank_user:
            user_log = "active"
    elif choice == "3":
        deleted = delete_account()
        if deleted and bank_user == deleted:
            bank_user = None
            user_log = None
    else:
        print("⚠️ Invalid option!")

    if bank_user:
        print(f"🔥 Current user: {bank_user}")
    else:
        print("🚪 No user logged in.")

    print(f"📌 user_log = {user_log}")

