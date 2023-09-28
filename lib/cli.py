#!/usr/bin/env python3

import ipdb
import sqlite3
from helpers import *
from mainmenu import *


if __name__ == "__main__":
    main_menu()
    ipdb.set_trace()


def get_option_description(option_id):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT option_description FROM options WHERE option_id = ?", (option_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return None


def get_scene_description(scene_id):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT scene_description FROM scenes WHERE scene_id = ?", (scene_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return None


def introduction():
    scene_0_description = get_scene_description(0)
    option_1_description = get_option_description(1)
    option_2_description = get_option_description(2)
    print_slowly(f"""
          {scene_0_description}
          
          Option 1: {option_1_description}
          
          Option 2: {option_2_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        introchoice = int(input('>>> '))
        handle_introduction(introchoice)
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def handle_introduction(introchoice):
    if introchoice == 1:
        game_over()
    elif introchoice == 2:
        outside_the_party()
    else:
        print("Make a valid selection")
        return


def outside_the_party():
    scene_1_description = get_scene_description(1)
    option_3_description = get_option_description(3)
    option_4_description = get_option_description(4)
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
        handle_outside_the_party_choice(outside_the_party_choice)
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def handle_outside_the_party_choice(outside_the_party_choice):
    if outside_the_party_choice == 1:
        game_over()
    elif outside_the_party_choice == 2:
        following_the_cat()
    else:
        print("Make a valid selection")
        return


def following_the_cat():
    scene_2_description = get_scene_description(2)
    option_5_description = get_option_description(5)
    option_6_description = get_option_description(6)
    print_slowly(f"""
          
          {scene_2_description}

          Option 1: {option_5_description}
          
          Option 2: {option_6_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        following_the_cat_choice = int(input('>>> '))
        handle_following_the_cat_choice(following_the_cat_choice)
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def handle_following_the_cat_choice(following_the_cat_choice):
    if following_the_cat_choice == 1:
        the_encounter()
    elif following_the_cat_choice == 2:
        game_over()
    else:
        print("Make a valid selection")
        return


def the_encounter():
    scene_3_description = get_scene_description(3)
    option_7_description = get_option_description(7)
    option_8_description = get_option_description(8)
    print_slowly(f"""
          
          {scene_3_description}
          
          Option 1: {option_7_description}
          
          Option 2: {option_8_description}

          Which option do you choose? 1 or 2?
          """)

    try:
        the_encounter_choice = int(input('>>> '))
        handle_the_encounter_choice(the_encounter_choice)
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def handle_the_encounter_choice(the_encounter_choice):
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


def game_over():
    print_slowly("Game Over...")
    print("Type 0 to return to the main menu.")
    print("Type 1 to return to start a new game.")
    print("Type 2 to start from the previous scene.")

    try:
        game_over_choice = int(input('>>> '))
        handle_game_over_choice(game_over_choice)
    except ValueError:
        print("Please enter a valid number (0, 1, or 2).")


def handle_game_over_choice(game_over_choice):
    if game_over_choice == 0:
        pass  # function to return to main menu
    elif game_over_choice == 1:
        introduction()
    elif game_over_choice == 2:
        pass  # function to start from previous scene based on player_scene_id
    else:
        print("Make a valid selection")
        return
