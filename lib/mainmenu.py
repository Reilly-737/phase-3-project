import ipdb 
import helpers 


class MainMenu:
    def __init__(self):
        self.player_name = None 
    def display_menu(self):
        
        print("~~~~~~", GAME_TITLE, "~~~~~~")
        print(GAME_INSTRUCTIONS)
        print("1. Enter Player")
        print("2. Quit")
        
    def start(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            
            if choice == '1':
                self.enter_player()
            elif choice == '2':
                print ("Goodbye!")
                break 
            else: 
                print("Please select a valid option.")
                
    def enter_player(self):
        player_name = input("Enter player name: ")
        self.player_name = player_name
        print(f"Welcome, {self.player_name}!")
        
        while True: 
            choice = input("Start a new game (new). Continue current game(con). Delete current game(del). Exit(exit).")
            
            if choice == "new":
                helpers.start_new_game(player_name)
                break
            elif choice == "con":
                helpers.continue_game(player_name)
                break
            elif choice == "del":
                helpers.delete_game_data(player_name)
                break
            elif choice == "exit":
                helpers.exit_program()
                break
            else:
                print("Whoops! Invalid choice. Please Select a valid option.")
        
        #helpers.delete_player(player_name)
        
        #choice = input("Do you want to exit the game? (yes/no): ")
        #if choice.lower() == "yes": 
         #   helpers.exit_game()
          #  exit()

GAME_TITLE = "The Ominous Encounter"
GAME_INSTRUCTIONS = """
Welcome! 
Instructions 
 Select "Enter Player" to start or continue your adventure.
 If you have a recorded name, you can choose to start a new game 
    or continue your current game.
    (enter more info here )
"""

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.start()
    
ipdb.set_trace()