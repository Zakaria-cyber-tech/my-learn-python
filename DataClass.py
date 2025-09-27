import os
import time
from dataclasses import dataclass
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

@dataclass
class User:
    name: str
    age: int
    id: int
    email:str

class Users_proj:
    def inp_user(self):
        name=input("Ener Your Name:  ")
        while True:
            age=input("Enter Your Age(Digit):  ")
            if age.isdigit() and int(age) < 100:
                break
            else:
                print("Pleas Enter Number(lower than 100).")
        while True:
            id=input("Enter The ID Num(A Three Boxes):  ")
            if id.isdigit() and len(id)==3:
                break
            else:
                print("Pleas Enter A number and 3 Boxes.")
        email=input("Enter Your Email Without(@exampel.com)")+"@ouar.com"

        return User(name,int(age),id,email)
    def display(self,user=User):
        print(f"The Name Is {user.name}")
        print(f"The age of User IS:{user.age}")
        print(f"The Id Of User is:{user.id}")
        print(f"The email of The User is: {user.email}")
proj=Users_proj()
user1=proj.inp_user()
time.sleep(2)
print("_"*20)
proj.display(user1)