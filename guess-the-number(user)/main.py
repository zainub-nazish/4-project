import random

print("Welcome to the  Number Guessing Game!")

secret_number = random.randint(1, 10)
print("I have secret a number between 1 and 10.Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("To high! Try again.")
        elif guess < secret_number:
            print("To low! Try again.")
        else:
            print("Congratulation! You've guessed the number!") 
            break

    except ValueError:
        print("Invalid input.Please enter a number between 1 and 10.")       