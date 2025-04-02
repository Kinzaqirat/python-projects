import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower = 1  # Lower bound
    upper = 100  # Upper bound
    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"I have selected a number between {lower} and {upper}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower or guess > upper:
                print(f"❌ Please guess within the range {lower}-{upper}.")
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Run the game
while True:
    play_game()
    replay = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
