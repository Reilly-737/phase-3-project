# lib/helpers.py

import time


def helper_1():
    print("Performing useful function#1.")


def game_over():
    print("Game over. Goodbye!")
    exit()


def head_outside():
    print("You're outside!")


def exit_program():
    print("Goodbye!")
    exit()


def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()
