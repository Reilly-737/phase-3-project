#!/usr/bin/env python3

#import ipdb
from helpers import *
from mainmenu import *
from models.model_1 import *


if __name__ == "__main__":
    initialize_database()
    main_menu()
    ipdb.set_trace()


def display_scene_description(scene_id):
    scene = Scenes.get(Scenes.scene_id == scene_id)
    return (scene.scene_description)


def display_option_description(option_id):
    option = Options.get(Options.option_id == option_id)
    return (option.option_description)




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
    #print_slowly_centered(introduction)

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
   # print_slowly_centered(introduction)

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
    scene_2_description = display_scene_description(2)
    option_5_description = display_option_description(5)
    print_slowly(f"""

          {scene_2_description}

          {option_5_description}
          
          """)

    try:
        following_the_cat_choice = int(input('>>> '))
        handle_following_the_cat_choice(following_the_cat_choice)
    except ValueError:
        print("Please enter a valid number (1 or 2).")


def handle_following_the_cat_choice(following_the_cat_choice):
    if following_the_cat_choice == 1:
        the_encounter()
    else:
        print("Make a valid selection")
        return


def the_encounter():
    scene_3_description = display_scene_description(3)
    option_6_description = display_option_description(6)
    option_7_description = display_option_description(7)
    print_slowly(f"""

          {scene_3_description}

          Option 1: {option_6_description}

          Option 2: {option_7_description}

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
        print()
        game_over_message = """
            Ooze (telepathically): 
            Very well, seeker of knowledge. Your fate is written on the canvas of time.
            The eye's gaze intensifies, and before you can react, it knocks you out. 
            When you wake up, you find yourself on the porch, a prophecy etched onto the inside of your arm,
            your mind forever marked by the encounter."""
        print()
        random_prophecy = get_random_prophecy()
        
        print_somewhat_fast(game_over_message)
        print()
        print_slowly(random_prophecy)
        print()
    else:
        print("Make a valid selection or death and destruction await you.")
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
