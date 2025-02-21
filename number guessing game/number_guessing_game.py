# number guessing game
import random  # to generate random num

number= random.randint(1,30) #randit to generate  btw 1 to 30

guess=0

print("WELCOME TO NUMBER GUESSING GAME🔢")

while guess != number:
    guess= int(input("Guess num btw 1 to 30 : "))
    if(guess>number):
        print("TOO HIGHER!")
    elif(guess<number):
        print("TOO LOWER!") 
    else:
        print("YOU WON")     

