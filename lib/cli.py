#!/usr/bin/env python3

import ipdb
from helpers import *
from mainmenu import *
from models.model_1 import *

if __name__ == "__main__":
    initialize_database()
    main_menu()
    ipdb.set_trace()


def introduction():
    scene_0_description = display_scene_description(0)
    option_1_description = display_option_description(1)
    option_2_description = display_option_description(2)
    print_slowly(f"""
          {scene_0_description}

          Option 1: {option_1_description}

          Option 2: {option_2_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        introchoice = int(input('>>> '))
        if introchoice == 1:
            game_over()
        elif introchoice == 2:
            outside_the_party()
        else:
            print("Make a valid selection")
            return
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def outside_the_party():
    scene_1_description = display_scene_description(1)
    option_3_description = display_option_description(3)
    option_4_description = display_option_description(4)
    print_slowly(f"""
          You sip on lemonade, savoring the refreshing taste as you engage in
          delightful conversations with your friends. At one point, you decide to
          step outside for a quick vape break.

          {scene_1_description}

          Option 1: {option_3_description}

          Option 2: {option_4_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        outside_the_party_choice = int(input('>>> '))
        if outside_the_party_choice == 1:
            game_over()
        elif outside_the_party_choice == 2:
            following_the_cat()
        else:
            print("Make a valid selection")
            return
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def following_the_cat():
    scene_2_description = display_scene_description(2)
    option_5_description = display_option_description(5)
    option_6_description = display_option_description(6)
    print_slowly(f"""

          {scene_2_description}

          Option 1: {option_5_description}

          Option 2: {option_6_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        following_the_cat_choice = int(input('>>> '))
        if following_the_cat_choice == 1:
            the_encounter()
        elif following_the_cat_choice == 2:
            game_over()
        else:
            print("Make a valid selection")
            return
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def the_encounter():
    scene_3_description = display_scene_description(3)
    option_7_description = display_option_description(7)
    option_8_description = display_option_description(8)
    print_slowly(f"""

          {scene_3_description}

          Option 1: {option_7_description}

          Option 2: {option_8_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        the_encounter_choice = int(input('>>> '))
        if the_encounter_choice == 1:
            game_over()
        elif the_encounter_choice == 2:
            print_slowly("""As the moon wanes, so too must all things find their end.
                        But from the ashes of mortality, the phoenix of rebirth shall rise,
                        ushering in a new chapter of your eternal journey.""")
            # when done, switch to function for the random prophecy
        else:
            print("Make a valid selection")
            return
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def game_over():

    print_somewhat_fast("""
  ▄████  ▄▄▄      ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄   ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄ ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒  ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░      ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                    ░



                        """)

    print("Type 0 to return to the main menu.")
    print("Type 1 to return to start a new game.")
    print("Type 2 to start from the previous scene.")

    try:
        game_over_choice = int(input('>>> '))

        if game_over_choice == 0:
            from mainmenu import main_menu
            main_menu()
        elif game_over_choice == 1:
            print_slowly("""
                  Starting a new game...
                  """)
            introduction()
        elif game_over_choice == 2:
            pass
        else:
            main_menu()

    except ValueError:
        print("Please enter a valid number (0, 1, or ")
