import random
import string
symbol=string.punctuation
total=int(input("Enter the the total number of pasword generators:\n"))
number_characters=int(input("Enter the number of character in password:\n"))
number_numbers=int(input("Enter the number of numbers in your password:\n"))
number_sumbols=int(input("Enter the number of sumbols in your password:\n"))
if number_characters + number_numbers + number_sumbols > total:
    print(f"the total numbers of characters, numbers and symbols should not exceed {total}")
else:
    password=[]
    c=string.ascii_letters
    c=random.choices(c,k=number_characters)
    password += c
    n=random.choices(string.digits,k=number_numbers)
    password += n
    s=random.choices(symbol,k=number_sumbols)
    password += s
    random.shuffle(password)
    password="".join(password)
    print(f"the over password is: {password}")
    print("Prees  enter to exit")
    input()
    exit()