import random

stages = ['''
    ---------
    |       |
    |         
    |
    |
    |
     -------- 
''', 
'''
    --------
    |       |
    |       O
    |
    |
    |
    --------
    ''',
    '''
    -------
    |      |
    |      O
    |      |
    |
    |
    --------
    ''',
    '''
    ---------
    |        |
    |        O
    |       /|
    |
    |
    ---------
    ''',
    '''
    ---------
    |        |
    |        O
    |       /|\\
    | 
    |
    ---------
    ''',
    '''
    ---------
    |        |
    |        O
    |       /|\\
    |       /
    |
    ----------
    ''',
    '''
    ----------
    |         |
    |         O
    |        /|\\
    |        /  \\
    |
    ----------
    ''']

words =['apple','banana','orange','graph','watermelon','kiwi','mango','peach','pear','pulm','berry']

chosen_word = random.choice(words)
words_display = ['_' for _ in chosen_word]
guess_letters = []
lives = len(stages)-1

print("Welcome to Hangman!")
print("Guess the fruits word.")

while True:
    print(" ".join(words_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.\n")
        continue
    if guess in guess_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                words_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) -lives -1])
        lives -= 1
        print(f"You have {lives} lives left.")

        if lives == 0:
            print(stages[lives])
            print(f"You lost! The word was '{chosen_word}'.")
            break        


    