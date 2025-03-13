#Hangman.py
import random 
import os

hangman_figure = ['''
+---+
  |   |
  o   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /    |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
def hangman():
    word_list = ["lily","banana","apple","grapes","orange"]
    word = random.choice(word_list).lower()
    lives = 5
    display = "_" *len(word)
    already_guessed = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Hangman!")
        print(display)
        print(f"Lives: {lives}")
        print("Already guessed:", ", ".join(already_guessed))
        guess = input("Guess a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in already_guessed:
            print("The letter was already guessed by you -_-")
            continue
        already_guessed.append(guess)
        if guess in word:
            print("Correct!")
            word_as_list = list(display)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            display = "".join(word_as_list)
            if "_" not in display:
                print("Wooo,You Guessed It ^.^ ", word)
                break
        else:
            print("Incorrect!")
            lives -= 1
            print(hangman_figure[lives])
            if lives == 0:
                print("You are dead >_< . The word was:", word)
                break
    play_again = input("Do you want to play again? ^>^(y/n): ").lower()
    if play_again == "y":
        hangman()
if __name__ == "__main__":
    hangman()