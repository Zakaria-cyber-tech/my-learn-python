import random
data=""
print("Welcome To the 'SPIN' game:\n")
def spin():
    names=input("Enter the name of your Friend sipared ba comma:\n").split(",")
    names=random.choice(names)
    for i in range(3):
        print("Loding....")
    print("the name is:")
    print(f"**{names}**")
    data.append(names)
spin()
rounds=1
while "y" in input("Are you retry,Enter (Y)To yes or (N) To no:\n").lower():
    rounds+=1
    print(f"******Round:{rounds}******")
    spin()

show=input(f"Are you show data games:\n")
if show=="yes":
    print(f"thi is Data:{data}")
else:
    print("OK...")
    exit()
