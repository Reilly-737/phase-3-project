
from helpers import *
from cli import *
import readline


def main_menu():

    print_somewhat_fast(game_title)
    print_slowly(game_instructions)

    while True:
        print("""



                                                    ----------------------------
                                                    1. Enter Player Name
                                                    ----------------------------
                                                    2. Delete Player Name
                                                    ----------------------------
                                                    3. Display All Player Names
                                                    ----------------------------
                                                    4. Edit Player Name
                                                    ----------------------------
                                                    5. Quit
                                                    ----------------------------
                                                    """)

        print("""


            """)

        input_message = "Select an option: "
        print_slowly(input_message)
        choice = input()

        print("""


            """)

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

                        ~~Instructions~~

    *Select "Enter Player" to start or continue your adventure.

    *Follow the story's choices carefully and make decisions to uncover your fate.

    *Enjoy the experience and see where your choices lead you. Good luck!
"""
