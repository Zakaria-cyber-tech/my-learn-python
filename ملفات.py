import time

num_words=0
while True:
    fn=input("Enter The Name of File:  ")
    with open(fn,"a",encoding="utf-8") as f:
        fz=input("Enter the consept (Enter 'Read' To exit):  ").lower()
        f.write(f"{fz}\n")
        if fz=="read":
            with open(fn,"r") as h:
                print(h.read())
                num_line=h.readlines()
                for i in f"{fn}.txt":
                    num_words+=len(i.split())
                print(f"The num of lines is:{num_line}")
                print(f"The num of words is:{num_words}")
            time.sleep(6)
            exit()
