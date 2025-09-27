import random
work=["good","bad","hi"]
work_ran=random.choice(work)
space=["_"] * len(work_ran)
print(" ".join(space))
moha=6
#العرض
kawa3id=input("Enter any string to show kawa3id(prees Enter to skep:)")
if kawa3id:
    print(f"ktab character wa7ad wa ila radi t3a9ab:")
    print(f"mat7awalch trach:")
while "_" in space and moha > 0:
    gess=input("gess a (1) character: \n").lower()
    if len(gess) >1:
        print(f"radi tn9ass {len(gess)} mohawalat  7it 5assak tktab rir 1 character")
        moha-=len(gess)-1
    if gess not in work_ran:
        moha -=1
    for i in range(len(work_ran)):
        if work_ran[i]== gess:
            space[i] = gess
    print(f"**{" ".join(space)}**")
    print(f"you have {moha} chances left")
if "_" not in space:
    print("************you win***********")
else:
    print("************you lose**********")