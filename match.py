import random

class Match:
    def __init__(self):
        self.player1_name = ""
        self.player2_name = ""


    def gesture_list(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        return self.options

    def player_choice(self):
        choice = input('What do you choose? \nA) Rock \nB) Paper \nC) Scissors \nD) Lizard \nE) Spock \nPlease select A, B, C, D, or E:  ')
        while True:
            if choice == 'A' or choice == 'a':
                choice = self.options[0]
            elif choice == 'B' or choice == 'b':
                choice = self.options[1]
            elif choice == 'C' or choice == 'c':
                choice = self.options[2]
            elif choice == 'D' or choice == 'd':
                choice = self.options[3]
            elif choice == 'E' or choice == 'e':
                choice = self.options[4]
            if choice in self.options:
                print(f"Player has chosen {choice}")
                break
            else:    
                choice = input('Invalid choice, please try again. \nA) Rock \nB) Paper \nC) Scissors \nD) Lizard \nE) Spock \nPlease select A, B, C, D, or E:  ')
        
    def play_round(self):
        round_won = 0
        while round_won < 2:
            if player_1.choice == self.options[0]:
                
        # self.gesture_list()
        # self.player_choice()

        
    def display_welcome(self):
        print("\n*----------------------------------*")
        print("Welcome to RSPLS!")
        print("*----------------------------------*\n")
        print("The Rules of the game are as follows:\n")
        print("Rock beats Scissors & Lizard!\nScissors beats Paper & Lizard!\nSpock beats Rock & Scissors!\nLizard beats Spock & Paper\nPaper beats Rock & Spock!\n")
        print("When either a Player or the AI wins a best 2 out of 3 rounds, they are the winners!\n ")
        

