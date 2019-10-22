import random
import time

"""Below is a list of secret words that can be expanded"""
hangman_words = [
    "snail", "lion"
]

guess_letter = []
secret_word = random.choice(hangman_words)
print(secret_word)
secret_word_len = len(secret_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
name = str(input("What is you name?\n"))
print(f"Hello {name}")


def introduce():
    """Randomize a secret word and small introduction"""
    for character in secret_word:
        guess_letter.append("_")
    print("Let's Play!")
    print("Secret word is ", secret_word_len, " letter long")
    time.sleep(2)
    print("You can guess a-z letter. Remember! Only one letter each round!\n")
    time.sleep(2.8)


def guessing():
    shots = 1
    """ Definition of play. You have 10 chances which are lower when you type bad letter"""
    while shots < 10:
        guess = input("Give me letter\n").lower()
        if guess not in alphabet:  # Check if it s correct letter
            print("Sorry that's not allow sign. Please chose from a-z alphabet\n")
        if guess in secret_word:  # Letter in secret word
            print("Yeah!\n")
            print(f"You have {10 - shots} chances left")

            for element in range(0, secret_word_len):
                if secret_word[element] == guess:
                    guess_letter[element] = guess
                    print(guess_letter)  # Reveal of correct letter
            if "_" not in guess_letter:
                print("Congratulation! You WON!\n")
                break
        else:
            print("Too bad. Wrong guess! Try again!\n")
            shots += 1
            print(f"You have {10 - shots} chances left")

            if shots == 10:
                print("You are HANGED!\n")
                break


"""Special key to lunch app"""
if __name__ == '__main__':
    introduce()
    guessing()
