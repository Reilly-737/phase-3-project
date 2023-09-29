#!/usr/bin/env python3

# import ipdb
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
            game_over(1)
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
          {scene_1_description}

              Option 1: {option_3_description}

              Option 2: {option_4_description}

            Which option do you choose? 1 or 2?
          """)
   # print_slowly_centered(introduction)

    try:
        outside_the_party_choice = int(input('>>> '))
        if outside_the_party_choice == 1:
            game_over_id = 2
            game_over(game_over_id)
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
    print_slowly(f"""

          {scene_2_description}

            {option_5_description}

          """)

    try:
        following_the_cat_choice = int(input('>>> '))
        if following_the_cat_choice == 1:
            the_encounter()
        else:
            print("Make a valid selection")
            return

    except ValueError:
        print("Please enter a valid number (1 or 2).")


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

              
            print_somewhat_fast("""
   _______.-. .-. .--. .-. .-.,-. .-.  .---.                               
  |__   __| | | |/ /\ \|  \| || |/ /  ( .-._)                              
    )| |  | `-' / /__\ \   | || | /  (_) \                                 
    (_) |  | .-. |  __  | |\  || | \  _  \ \                                
      | |  | | |)| |  |)| | |)|| |) \( `-'  )                               
      `-'  /(  (_)_|  (_)(  (_)|((_)-'`----'                                
          (__)         (__)    (_)                                          
    ,---. .---. ,---.     ,---. ,-.      .--.-.   .-.,-..-. .-.  ,--,  .-.  
    | .-'/ .-. )| .-.\    | .-.\| |     / /\ \ \_/ )/|(||  \| |.' .'   |  ) 
    | `-.| | |(_) `-'/    | |-' ) |    / /__\ \   (_)(_)|   | ||  |  __| /  
    | .-'| | | ||   (     | |--'| |    |  __  |) (   | || |\  |\  \ ( _)/   
    | |  \ `-' /| |\ \    | |   | `--. | |  |)|| |   | || | |)| \  `-) |    
    )\|   )---' |_| \)\   /(    |( __.'|_|  (_)(_|   `-'/(  (_) )\____(_)   
   (__)  (_)        (__) (__)   (_)          (__)      (__)    (__)         
                   """)
            print()
            print_slowly("""
        In the dark recesses of your choices, the game concludes. 
        Yet in the shadows, infinite narratives linger. 
        Restart, and let the eerie echoes of your decisions haunt your next journey.
                         """)
            

        else:
            print("Make a valid selection or death and destruction await you.")
            return
    except ValueError:

            print("Please enter a valid number (1 or 2).")  



def game_over(game_over_id):

    print_slowly(game_over_description(game_over_id))
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



  