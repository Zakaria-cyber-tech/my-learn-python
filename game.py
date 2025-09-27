import random
print("Welcome to game: Rock, Paper, Scissors!")
input("Press Enter to start the game...")
print(f"your choise:rock or paper or scissors")
choise=["Rock", "Paper", "Scissors"]
hes_choise=input(f"Enter Rock or Paper or Scissors:\n").capitalize()
if hes_choise not in choise:
    print(f"sorry, your choise is not valid")
computer= random.choice(choise)
if hes_choise == computer:
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => It's a tie!")
if hes_choise== "Rock" and computer == "Scissors":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You win!")
if hes_choise=="Paper" and computer == "Rock":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You win!")
if hes_choise=="Scissors" and computer == "Paper":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You win!")
if hes_choise=="Rock" and computer == "Paper":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You lose!")
if hes_choise=="Paper" and computer == "Scissors":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You lose!")
if hes_choise=="Scissors" and computer == "Rock":
    print(f"Your choise: {hes_choise}, Computer choise: {computer} => You lose!")
input(f"Press Enter to exit the game...")