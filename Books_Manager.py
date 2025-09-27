import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#....................Start Class...............................
class Books:
    def __init__(self,title,author,id,status):
        self.title=title
        self.author=author
        self.id=id
        self.status=status
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"author: {self.author}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")
    
    def change_status(book_list):
        while True:
            inp_change=input("Enter The New Status:  ")
            if inp_change in ["active","inactive"]:
                IDD=input("Enter The ID Of Book:  ")
                if not book_list:
                    print("The Library is clean.")
                for c in book_list:
                    if c.id==IDD:
                        c.status==inp_change
                    print("The The Book Status is change")
                else:
                    print(f"This ID {IDD} is Not Found.")
                
                break
            else:
                print("Enter 'active' Or 'Inactive' please.")
        time.sleep(1)



class menu:
    def choises():
        print(f"1-Add New Book.\n2-Show All Books.\n3-Search In Books.\n4-change Status.\n5-Exit.")
    def main(self):
        man=menu()
        clear()
        man.choises()
#...................End Class........................

def creat_user():
    title=input("Enter The Title of Book:  ")
    clear()
    author=input("Enter The author of Book: ")
    clear()
    while True:
        id=input("Enter The ID:  ")
        if id.isdigit():
            break
        else:
            print(f"Enter A Number.")
            time.sleep(1)
    clear()
    while True:
        status=input("Enetr The Status Of Book(Press Enter To Skep):  ").lower()
        if status:
            if status in ["active","inactive"]:
                break
            else:
                print("Pleas Enter active Or inactive")
        else:
            status="inactive"
            break
    print("The Book Is Added.....")
    time.sleep(1)
    clear()
    return Books(title,author,id,status)

def search_book(book_list):
    print("1-Search on Title.\n2-Search on ID.\n3-search on status.\n4-BACK_Menu.")
    choice2=input("Enter Your choice:  ")
    if choice2=="1":
        tl=input("Enter The Title Of Thr Book:  ")
        if not book_list:
            print("The Library is clean.")
        for b in book_list:
            if b.title==tl:
                print("_"*20)
                b.display()
                print("_"*20)
        time.sleep(5)
    elif choice2=="2":
        IDD=input("Enter The ID For Book:  ")
        if not book_list:
            print("The Library is clean.")
        for c in book_list:
            if c.id==IDD:
                print("_"*20)
                c.display()
                print("_"*20)
        time.sleep(5)
    elif choice2=="3":
        stat=input("Enter The Status Of The Book:  ")
        if not book_list:
            print("The Library IS Clean.")
        for d in book_list:
            if d.status==stat:
                print("_"*20)
                d.display()
                print("_"*20)
        time.sleep(5)
    elif choice2=="4":
        print("Exit Is Looding.....")
        time.sleep(1)
        menu.choises()
    else:
        print("Invalid Choice.")

def show_book(book_list):
    if not book_list:
        print("The Library is clean.")
    for l in book_list:
        print("_"*20)
        l.display()
        print("_"*20)
    time.sleep(10)
    clear()
#Body And project
book_list=[]
def body():
    while True:
        clear()
        
        menu.choises()
        choice=input("Enter Your choice:  ")
        if choice=="1":
            clear()
            book_list.append(creat_user())
        elif choice=="2":
            clear()
            show_book(book_list)
        elif choice=="3":
            clear()
            search_book(book_list)
        elif choice=="4":
            clear()
            Books.change_status(book_list)
            clear()
        elif choice=="5":
            print("chicking out...")
            clear()
            time.sleep(2)
            exit()
        else:
            if choice.isdigit() and choice not in ["1","2","3","4","5"]:
                print(f"{choice} is out of choises")
                time.sleep(2)
            else:
                print("Invalid Input.")
                time.sleep(1)
            

body()