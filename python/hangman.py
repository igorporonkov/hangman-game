#!/usr/bin/env python3
import random

words = [
    "python", "developer", "github", "hangman", "computer",
    "keyboard", "monitor", "internet", "software", "hardware"
]

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    return stages[attempts]

def main():
    word = random.choice(words).upper()
    guessed = set()
    incorrect = set()
    attempts = 7

    print("\n=== HANGMAN ===")

    while attempts > 0:
        print(display_hangman(attempts))
        print("\nWord:", " ".join([c if c in guessed else "_" for c in word]))
        print("Wrong guesses:", " ".join(incorrect) if incorrect else "None")
        guess = input("\nGuess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed or guess in incorrect:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print("Good guess!")
            if all(c in guessed for c in word):
                print(f"\n🎉 You won! The word was {word}. 🎉")
                break
        else:
            incorrect.add(guess)
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
            if attempts == 0:
                print(display_hangman(0))
                print(f"\n💀 Game over! The word was {word}. 💀")

if __name__ == "__main__":
    main()
