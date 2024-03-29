import random
import re

win_count = 0
lost_count = 0


def start_game(max_attempt):
    global win_count
    global lost_count

    words = ['javascript', 'python', 'java', 'swift']
    word = random.choice(words)
    mask_word = "-" * len(word)
    guess_char = []

    while True:

        if max_attempt <= 0:
            lost_count = lost_count + 1
            print("You lost!")
            break

        if '-' not in mask_word:
            win_count = win_count + 1
            print(word)
            print(f"You guessed the word {word}!")
            print("You survived!")
            break

        print(mask_word)
        answer = input("Input a letter: ")

        if not answer or len(answer) > 1:
            print("Please, input a single letter.")
            continue

        if not re.match('^[a-z]$', answer):
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        char = answer[0]

        if char in guess_char:
            print("You've already guessed this letter.")
            continue

        guess_char.append(char)

        if char in word:
            indexes = [index for index, c in enumerate(word) if c == char]

            text = list(mask_word)

            for index in indexes:
                text[index] = char

            mask_word = "".join(text)
        else:
            print("That letter doesn't appear in the word.")
            max_attempt = max_attempt - 1


def show_result():
    print("You won: {count} times.".format(count=win_count))
    print("You lost: {count} times.".format(count=lost_count))


while True:
    print("H A N G M A N")
    action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if action == 'play':
        start_game(8)
    elif action == 'results':
        show_result()
    elif action == 'exit':
        break
