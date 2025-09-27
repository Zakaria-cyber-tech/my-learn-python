import json
import os

FILE = "C:\\Users\\Zaka-PC\\Desktop\\json files project\\user.json"

cl = input("If You want clear The File Enter Any Alphabet(Press Enter To skip) ")
if cl:
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

choice = input("Enter 1 To create User, And 2 To load Users: ")

if choice == "1":
    # نقرأ اللائحة ديال users من الملف
    users = []
    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        with open(FILE, "r", encoding="utf-8") as f:
            users = json.load(f)

    # نطلب معلومات user جديد
    na = input("Enter Your name: ")
    la = input("Enter Your Last name: ")
    num = input("Enter Your 'ID': ")

    data = {
        "first_name": na,
        "last_name": la,
        "id": num
    }

    # نزيدو للائحة
    users.append(data)

    # نكتب اللائحة كاملة من جديد
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

elif choice == "2":
    if os.path.exists(FILE) and os.path.getsize(FILE) > 2:
        with open(FILE, "r", encoding="utf-8") as f:
            users = json.load(f)

        
        for u in users:
            print("-"*20)
            print(f"First Name: {u['first_name']}\nLast Name: {u['last_name']}\nID: {u['id']}")
            print("-"*20)
    else:
        print("File is empty.")
else:
    print("Invalid input.")
