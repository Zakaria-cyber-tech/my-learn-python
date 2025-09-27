maham=input("Enter your tasks separeted by commas: \n").split(",")
tam=[]
lam=[]
for x in maham:
    print("__________________________________________________________________________")
    print("++"+ x + "++")
    A=input("did you finishing this task? (yes/no): \n").lower()
    if A=="yes":
        print("Good job!")
        tam.append(x)
    elif A=="no":
        print("You need to finish this task!")
        lam.append(x)
    else:
        print("Invalid input, please enter yes or no.")
total=input("Do you want to see the total tasks? (yes/no): \n").lower()
if total=="yes":
    print(" ")
    print(f"++++++++++++++++++++tasks finished: +++++++++++++++++++++")
    print(" ")
    print(" ")
    print(tam)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(f"++++++++++++++++++++tasks not finished: +++++++++++++++++++++")
    print(" ")
    print(" ")
    print(lam)
input("Press Enter to exit the program...")
print("Thank you for using the task manager!")
