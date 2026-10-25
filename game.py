
import random

difficulty = input("Choose difficulty:\n" "Easy(1) 10 tries\n" "Medium(2) 7 tries\n" "Hard(3) 5 tries\n " "Enter your choice (1, 2, or 3): ")

if difficulty == "1":
    max_attempts = 10
    print ("You selected Easy!")

elif difficulty == "2":
    max_attempts = 7
    print ("You selected Medium!")

elif difficulty == "3":
    max_attempts = 5
    print ("You selected Hard! Good luck.")




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