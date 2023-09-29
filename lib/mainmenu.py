import ipdb
from helpers import *
from cli import *
import readline


def main_menu():

    print_somewhat_fast(game_title)
    print_slowly(game_instructions)

    while True:
        print("----------------------------")
        print("1. Enter Player Name")
        print("----------------------------")
        print("2. Delete Player Name")
        print("----------------------------")
        print("3. Display All Player Names")
        print("----------------------------")
        print("4. Edit Player Name")
        print("----------------------------")
        print("5. Quit")
        print("----------------------------")
        print()

        print()
        print()
        print()
        choice = input("Select an option: ")
        print()
        print()

        if choice == '1':
            print()
            create_player()
            introduction()
        elif choice == '2':
            print()
            delete_player()
        elif choice == '3':
            print()
            list_players()
        elif choice == '4':
            print()
            change_player_name()
        elif choice == '5':
            print()
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
