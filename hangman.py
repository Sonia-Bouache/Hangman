import nltk
import random
from nltk.corpus import words # type: ignore

nltk.download('words') # type: ignore


steps = [
    """    """,
    """=========""",
    """     
                     |
                     |
                     |
                     |
                     |
             =========""",
    """+---+
                     |
                     |
                     |
                     |
                     |
             =========""",
    """+---+
                 |    |
                      |
                      |
                      |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                      |
                      |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                 |    |
                      |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                /|    |
                      |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                /|\   |
                      |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                /|\   |
                /     |
                      |
              =========""",
    """+---+
                 |    |
                 O    |
                /|\   |
                / \   |
                      |
              ========="""
]

def get_random_word():
    word_list = words.words()
    return random.choice(word_list)

def play_hangman():
    word = get_random_word()
    word_length = len(word)
    blank = "-" * word_length
    step_n = 0
    blank_list = list(blank)
    completed = False

    print("Welcome to Hangman!")

    while not completed:
        user_input = input("Choose a letter: ").lower()

        if user_input in word:
            for i in range(word_length):
                if user_input == word[i]:
                    blank_list[i] = user_input
            blank = ''.join(blank_list)
        else:
            print(steps[step_n])
            step_n += 1
            if step_n == len(steps):
                print("YOU LOSE!")
                print(f"The word was: {word}")
                break

        print(blank)

        if "-" not in blank:
            print("YOU WON!")
            completed = True

play_hangman()
