import string
alphabet=string.ascii_lowercase
def all(txt,shift):
    chifra=""
    for i in txt:
        if i.lower() in alphabet:
            ind=alphabet.index(i.lower())
            new_position=(ind+shift)%26
            i=alphabet[new_position]
            if i.isupper():
                i.upper()
        chifra+=i
    print(chifra)
def zall(txt,shift):
    chifra=""
    for i in txt:
        if i.lower() in alphabet:
            ind=alphabet.index(i.lower())
            new_position=(ind-shift)%26
            i=alphabet[new_position]
            if i.isupper():
                i.upper()
        chifra+=i
    print(chifra)
print("+++TERMINAL+++")
choise=int(input(f"Enter A choise (Enter [1] to Encode);\n    (Enter [2] to decode):\n"))
if int(choise) == 1:
    all(input("Enter A string To Encode:\n"),int(input("Enter A shift number:\n")))
elif int(choise) == 2:
    zall(input("Enter A string To Decode:\n"),int(input("Enter A shift number:\n")))