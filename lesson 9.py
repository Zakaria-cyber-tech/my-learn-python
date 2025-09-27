import string
alphabet_up=string.ascii_uppercase
alphabet_down=string.ascii_lowercase
chifra=""
def all(inp,num):
    for i in inp:
        if i not in alphabet_up and alphabet_down:
            chifra+=i
            continue
        if (num) not in string.digits:
            print("this input incorrect.")
            break
        ind_up=(alphabet_up.index(i)+int(num))%26
        ind_down=(alphabet_down.index(i)+int(num))%26
        if i in alphabet_up:
            chifra+=alphabet_up[ind_up]
        else:
            chifra+=alphabet_down[ind_down]
    print(chifra)
zo=input("Enter the text: ")
z=input("Enter the number: ")
all(zo,z)
