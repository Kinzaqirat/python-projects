# GAME RULE!
# Rock beats scissors
# Scissors beats  paper
# Paper beats rock

import random

print("\n WECLOME 🎇")
choice=["rock ", "paper", "scissor"]
player=input("Chose Rock, Paper, Scissor : ").lower()
computer= random.choice(choice)
print(f"\n You chose {player} and computer chose {computer}\t")

if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("\nRock smashes scissors! You win😊!")
    else:
        print("\nPaper covers rock! You lose😟.")
elif player == "paper":
    if computer == "rock":
        print("\nPaper covers rock! You win😊!")
    else:
        print("\nPaper covers rock! You lose😟.")
 
elif player == "scissors":
    if computer == "paper":
        print("\nScissors cuts paper! You win😊!")
    else:
        print("\nPaper covers rock! You lose😟.")
       






