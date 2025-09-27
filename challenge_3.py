def Users_proj():
    import time
    import os
    def clear():
        os.system("cls" if os.name=="nt" else "clear")
    class User:
        def __init__(self,first,last,membership,status):
            self.first=first
            self.last=last
            self.membership=membership
            self.status=status
        def display(self):
            print(f"First name: {self.first}")
            print(f"Last name: {self.last}")
            print(f"The ID:{self.membership}")
            print(f"Status User: {self.status}")
    def create():
            first=input("Enter the First name:  ")
            last=input("Entar the last name:  ")
            membership=input("Enter the membership:  ")
            status=input("Enter the status user Or Press Enter To skip:  ")
            if not status:
                status="inactive"
            print("User is added...")
            return User(first,last,membership,status)
    user_list=[]
    
    #بدأ
    while True:
        clear()
        print("Welcome To user manegment..")
        print("1-add new User.\n2-show all Users\n3-sersh in Users\n4-Exit...")
        choice=input("Enter your choice:  ")
        if choice=="1":
            user_list.append(create())
            time.sleep(3)
            clear()
        elif choice=="2":
            if not user_list:
                print("The users is clean.")
                time.sleep(1)
                clear()
            else:
                for i in user_list:
                    print("_"*20)
                    i.display()
                    print("_"*20)
                time.sleep(15)
            clear()
        elif choice=="3":
            clear()
            print("Sersh by: ")
            print("1-ID.\n2-First name.\n3-Status.")
            choice2=input("Enter Your choice:  ")
            if choice2=="1":
                IDD=input("Enter The ID For sersh:  ")
                for x in user_list:
                    if x.membership==IDD:
                        print("_"*20)
                        x.display()
                        print("_"*20)
                    else:
                        break
                time.sleep(7)
                clear()
            elif choice2=="2":
                IDD=input("Enter The First name For sersh:  ")
                for x in user_list:
                    if x.first==IDD:
                        print("_"*20)
                        x.display()
                        print("_"*20)
                time.sleep(7)
                clear()
            elif choice2=="3":
                IDD=input("Enter The Status For sersh:  ").lower()
                for x in user_list:
                    if x.status==IDD:
                        print("_"*20)
                        x.display()
                        print("_"*20)
                time.sleep(7)
                clear()
        elif choice=="4":
            print("Exit is Looding...")
            time.sleep(2)
            break
        else:
            print(f"Incorrect Input,Try again..")

Users_proj()