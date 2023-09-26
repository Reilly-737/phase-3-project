# lib/cli.py

from helpers import (
    create_user, 
    login_user,
    delete_user_progress,
    exit_program
)
from models import initialize_database
from game_data import story_segment_1, story_segment_2, story_segment_3, story_segment_4, story_segment_5

initialize_database()
def start_game():
    pass #game logic goes here? Then make delete option? 

def main():
    user_authenticated = False 
    
    while True:
        print("Main Menu")
        print("1. Create Username")
        print("2. Login")
        
        if user_authenticated:
            print("4. Start Game")
        print("3.Exit")
        choice = input("> ")
        
        if choice == "1":
            username = input("Enter your username: ")
            if create_user(username):
                print("User created successfully!")
            else:
                print("Username already exists. Try a different one.")
        elif choice == "2":
            username = input("Enter your username: ")
            user = login_user(username)
            if user:
                print(f"Welcome back, {user[1]}!")
            else:
                print("Username not found. Please create a username.")
            user_authenticated = True
        elif choice == "4" and user_authenticated:
            start_game()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()
#delete needs to be added and an adjustment need to be made to the main menu. 
#Create username needs to go away when the login menu is out. 
#Make sure Create username also takes you to the game? Maybe? 