import os
import time
def clear():
    os.system("cls" if os.name=="nt" else "clear")
clear()
#class:
class user:
    def __init__(self,first,last,email,password,status):
        self.first=first
        self.last=last
        self.email=email
        self.password=password
        self.status=status
    def display(self):
        print(f"First name:{self.first}")
        print(f"Last Name: {self.last}")
        print(f"Email:{self.email}")
        print(f"password:{self.password}")
        print(f"status:{self.status}")
def create():
    first=input("Enter your first name:")
    last=input("Enter Your last name:")
    email=input("Enter Your Email:")
    password=input("Enter the password:")
    status=input("Enter the status of the user:")
    print("added successfully...")
    if status:
        pass
    else:
        status="inactive"
    time.sleep(2)
    clear()
    return user(first,last,email,password,status)
user_list=[]
while True:
    print("Welcome To the user Manager.")
    print("1-add new user.")
    print("2-Show all user.")
    print("3-Exit.")
    choice=input("Enter your choice: ")
    if choice=="1":
        user_list.append(create())
        time.sleep(3)
        clear()
    elif choice=="2":
        if user_list:
            print("displaying all user list...")
            time.sleep(1)
            for i in user_list:
                print("-"*20)
                i.display()
                print("-"*20)
            time.sleep(15)
            clear()
        else:
            print("sorry,The list is clean:")
        time.sleep(6)
        clear()
    elif choice=="3":
        print("Exit is Lood...")
        time.sleep(2)
        break
    else:
        print(f"invalaid Your choice:{choice}")
input("Click any key To 'Exit'..")
