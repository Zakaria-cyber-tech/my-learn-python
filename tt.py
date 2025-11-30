import random
import json
import os

def clear():
    os.system("cls" if os.name=='nt' else 'clear')
#start oop
class Books:
    def __init__(self,name, author, ID,status="/n"):
        self.name=name
        self.author=author
        self.ID=ID
        self.status=status
    def __str__(self):
        return f"name={name} \nauthor={author} \nID={ID} \nstatus={status}"

Books.name="Zakaria"
Books.author="Zaka"
Books.ID=214
print(Books)