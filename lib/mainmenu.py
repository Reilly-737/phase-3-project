# import ipdb
from helpers import *
from cli import *


def main_menu():
    print_somewhat_fast(game_title)
    print_slowly(game_instructions)
    print("1. Enter Player Name")
    print("2. Delete Player Name")
    print("3. Display All Player Names")
    print("4. Quit")

    while True:
        choice = input("Select an option: ")

        if choice == '1':
            create_player()
            introduction()
        elif choice == '2':
            delete_player()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option.")


game_title = """
▄▄▄█████▓ ██░ ██ ▓█████     ▒█████   ███▄ ▄███▓ ██▓ ███▄    █  ▒█████   █    ██   ██████    ▓█████  ███▄    █  ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒ ██  ▓██▒▒██    ▒    ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░  ██▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██░  ██▒▓██  ▒██░░ ▓██▄      ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██   ██░▒██    ▒██ ░██░▓██▒  ▐▌██▒▒██   ██░▓▓█  ░██░  ▒   ██▒   ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░ ████▓▒░▒██▒   ░██▒░██░▒██░   ▓██░░ ████▓▒░▒▒█████▓ ▒██████▒▒   ░▒████▒▒██░   ▓██░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░     ▒ ░▒░ ░ ░ ░  ░     ░ ▒ ▒░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░    ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
  ░       ░  ░░ ░   ░      ░ ░ ░ ▒  ░      ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░        ░      ░   ░ ░ ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░
          ░  ░  ░   ░  ░       ░ ░         ░    ░           ░     ░ ░     ░           ░        ░  ░         ░ ░ ░          ░ ░     ░              ░             ░  ░   ░
                                                                                                              ░
"""

game_instructions = """
Welcome!
Instructions
Select "Enter Player" to start or continue your adventure.
If you have a recorded name, you can choose to start a new game
or continue your current game.
Follow the story's choices carefully and make decisions to uncover your fate.
Enjoy the experience and see where your choices lead you. Good luck!
"""
