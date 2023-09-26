# lib/cli.py

from helpers import (
    exit_program,
    print_slowly,
    head_outside,
    game_over
)


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")

def first_option():
    while True:
        start_adventure()
        choice = input("> ")
        if choice == "0":
            game_over()
        elif choice == "1":
            head_outside()
        elif choice == "2":
            exit_program()
        else:
            print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Create a user")
#     print("1. Log in with existing username and password")


def start_adventure():
    print_slowly("""
          You find yourself amidst a vibrant party with your friends, 
          the music pulsating through the air as laughter fills the room. 
          You're faced with a choice: 
          
          """)
    print_slowly("""
                0. Join your friends for more shots and dive headfirst into 
                the night's revelry.
          
          """)
    print_slowly("""
                1. Opt for a more mellow approach, sipping on lemonade 
                as you enjoy the company of your friends.
          
          """)
    print_slowly("""
                2. Exit game.
          
          """)


if __name__ == "__main__":
    first_option()
