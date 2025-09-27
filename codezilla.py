import os
import time
def clear():
    os.system("cls" if os.name=="nt" else "Clear")
class Player:
    def __init__(self):
        self.name=""
        self.symbole=""
    def choose_name(self):
        while True:
            name=input("Enter Your name(letter only):  ")
            if name.isalpha():
                self.name=name
                break
            print("Enter A letter Please..")
    def choose_symbole(self):
        while True:
            symbole=input("Enter Your Symbole(letter Only):  ")
            if symbole.isalpha():
                self.symbole=symbole.upper()
            print("Pleas Enter A letter And 1 Alphabet")
class Menu:
    def display_main_menu(self):
        print("Welcome To [X],[O] Game.")
        while True:
            print("1-Start Game")
            print("2-Quit Game")
            num_choose=input("Enter Your Choice(1 or 2):  ")
            if num_choose.isdigit():
                print("OK")
                time.sleep(1)
                clear()
                return num_choose
            print("Pleas Enter 1 Or 2")