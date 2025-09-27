class door():
    color=""
    materials=""
    L=0
    l=0
def badroom_doors():
    badroom_door= door()
    badroom_door.color=input("Enter the color of bathroom door: ")
    badroom_door.materials=input("Enter the materials of bathroom door: ")
    badroom_door.L=int(input("Enter the 'L' of bathroom door: "))
    badroom_door.l=int(input("Enter the 'l' of bathroom door: "))
    print(badroom_door.color)
    print(badroom_door.materials)
    print(badroom_door.L)
    print(badroom_door.l)

def kitchen_doors():
    kitchen_door=door()
    kitchen_door.color=input("Enter the color of kitchen door: ")
    kitchen_door.materials=input("Enter the materials of kitchen door: ")
    kitchen_door.L=int(input("Enter the 'L' of kitchen door: "))
    kitchen_door.l=int(input("Enter the 'l' of kitchen door: "))
    print(kitchen_door.color)
    print(kitchen_door.materials)
    print(kitchen_door.L)
    print(kitchen_door.l)

def livingroom_doors():
    livingroom_door=door()
    livingroom_door.color=input("Enter the color of living room door: ")
    livingroom_door.materials=input("Enter the materials of living room door: ")
    livingroom_door.L=int(input("Enter the 'L' of living room door: "))
    livingroom_door.l=int(input("Enter the 'l' of living room door: "))
    print(livingroom_door.color)
    print(livingroom_door.materials)
    print(livingroom_door.L)
    print(livingroom_door.l)
#إكتمال الجسم
for i in range(3):
    inp=input("Do you want to start with the living room (choose 1), the kitchen (choose 2), or the bathroom (choose 3)?\n")

    if int(inp)==1:
        livingroom_doors()
    elif int(inp)==2:
        kitchen_doors()
    elif int(inp)==3:
        badroom_doors()
    else:
        print(f"Your choice {inp} is invalid...\n")