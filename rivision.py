import random
list=["yes","no"]
list_ran=random.choice(list)
if list_ran=="yes":
    with open("yes or no.txt","w") as var:
        var.write("The programing is the")
try:
    with open("yes or no.txt","r") as l:
        lili=l.read()
except FileNotFoundError:
    print("The File is clean:..")
input("Enter Any key")