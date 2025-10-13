import os
import time


library=[]
wishlist=[]
def clear():
    os.system('cls' if os.name=="nt" else 'clear')
def dilay(sec):
    try:
        time.sleep(sec)
    except Exception:
        print("time is not found..")
        time.sleep(2)


print(f"{"*"*10} Welcome to the Library {"*"*10}")
dilay(2)
clear()



