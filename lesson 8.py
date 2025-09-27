ascii=[
    '''
____
|/   |
|   
|    
|    
|    
|
|_____''',
'''
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____''',
'''
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____''',
'''
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____''',
'''
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____''',
'''
 ____
|/   |
|   (_)
|   \|/
|    |
|   | 
|
|_____''',
'''
 ____
|/   |
|   (_)
|   \|/
|    |
|   | |
|
|_____''',
'''
 ____
|/   |
|   (_)
|   |||
|    |
|   | |
|
|_____''']





import random
lit=["good", "bad","hi"]
list=random.choice(lit)
space=["_"] * len(list)
moha=6
مضى=[]
kawa3id=input("are you need showin kawa3id;Enter any string to to show (press Enter to skep):")
#العرض
if kawa3id:
    print("**************************")
    print("ktab character wa7ad wa ila radi t3a9ab:")
    print("mat7awalch trach:")
    print("**************************")
print(ascii[0])
print(" ".join(space))
while "_"in space and moha>0:
    gess=input("Enter A character:\n").lower()
    if gess in مضى:
        print(f"rah |{gess}| ktabtiha 9bal")
        continue
    مضى.append(gess)
    if len(gess)>1:
        print("5alafti l9awa3id radi tn9ass li 2 mohawalat")
        moha-=1
    if gess not in list:
        moha-=1
    for i in range(len(list)):
        if list[i]==gess:
            space[i]=gess
    print(ascii[6-moha])
    print(f"you have {moha} mohawalat")
    print(" ".join(space))
if moha>0:
    print("******You are Win******")
else:
    print("*******You Lose*******")
    print(f"the word was: {list}")
    print(ascii[6])
