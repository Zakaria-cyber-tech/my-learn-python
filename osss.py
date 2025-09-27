from challenge_3 import Users_proj
import os
import time
from turtle import Turtle,Screen
import getpass
admin=["Zakaria2025","moha0808","Zakaria12"]

def clear():
    os.system("cls" if os.name=='nt' else "clear")
clear()
inp=getpass.getpass("Enter The Password For Using:  ")
for i in admin:
    if i==inp:
        print("The password is Correct:")
        break
else:
    print("The password is Incorrect.")
    time.sleep(2)
    exit()

moha=Turtle("arrow")
moha.color("blue")
window=Screen()
window.setup(800,600)
window.bgcolor("orange")
moha.pensize(5)

name=window.textinput("Hello","What is Your name")
for _ in range(4):
    moha.forward(200)
    moha.left(90)
moha.write(name,font=15)


window.exitonclick()
time.sleep(2)

if not os.path.exists("File course"):
    os.mkdir("File course")
    print("The File is created.")
else:
    print("This File Exist..")
time.sleep(3)
Users_proj()
time.sleep(4)
