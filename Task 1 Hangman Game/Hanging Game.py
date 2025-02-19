# Daniyal Arain
# Task 1
# Hangman Game
# Design a text-based Hangman game. The program
# selects a random word, and the player guesses one
# letter at a time to uncover the word. You can set a
# limit on the number of incorrect guesses allowed.



import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'developer', 'engineer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Wrong guess.")
            attempts -= 1
    
    if attempts == 0:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
