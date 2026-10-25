
import random

difficulty = input("Enter your choice e.g. 1, 2, or 3: ")

if difficulty == "1":
    max_attempts = 10
else:
    print("Invalid choice. Please select 1, 2 or 3")
    max_attempts = 0

hidden_number = random.randint(1, 100)
attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == hidden_number:
        print("Correct! You guessed the number!")
        print(f"You used {attempts} attempt(s).")
        break

    elif guess > hidden_number:
        print("Too High, Guess lower")

    elif guess < hidden_number:
        print("Too Low, Guess Higher")

    remaining = max_attempts -  attempts
    print(f"You have {remaining} guesses left!")

else:
    if max_attempts > 0:
        print("GAME OVER! You have run out of guesses.")
        print(f"The correct number was {hidden_number}.")