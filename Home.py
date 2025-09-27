print("Hello gays welcome to my project")
print("choose your option")
rabbits=[["@" , "@", "@"], ["@", "@", "@"], ["@", "@", "@"]]
print(f"{rabbits[0]}\n{rabbits[1]}\n{rabbits[2]}")
local=input("enter ligne and location: \n")
satr=int(local[0])
col=int(local[1])
if satr<1 or col>3 :
    print("out of range")
    exit()
rabbits[satr-1][col-1]="*"
print(f"{rabbits[0]}\n{rabbits[1]}\n{rabbits[2]}")
input(f"PREES Enter to exit")
exit()
