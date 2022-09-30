import random
from human import Human
from ai import AI

class Match:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
        self.options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        
    def run_game(self):
        self.display_welcome()
        self.play_round()
        self.display_winner()

    def display_welcome(self):
        print("\n*----------------------------------*")
        print("Welcome to RSPLS!")
        print("*----------------------------------*\n")
        print("The Rules of the game are as follows:\n")
        print("Rock beats Scissors & Lizard!\nPaper beats Rock & Spock!\nScissors beats Paper & Lizard!\nLizard beats Spock & Paper\nSpock beats Rock & Scissors!\n")
        print("When either a Player or the AI wins a best 2 out of 3 rounds, they are the winners!")
        
    def play_round(self):
        while self.player1.rounds_won < 2 and self.player2.rounds_won < 2:
            print(f"\n{self.player1.name} has {self.player1.rounds_won} wins!\n{self.player2.name} has {self.player2.rounds_won} wins!\n")
            self.player1.choice = self.player1.choose_gesture()
            self.player2.choice = self.player2.choose_gesture()
            if self.player1.choice == self.options[0] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[3]):
                self.player1.round_win()
            elif self.player1.choice == self.options[1] and (self.player2.choice == self.options[0] or self.player2.choice == self.options[4]):
                self.player1.round_win()
            elif self.player1.choice == self.options[2] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[3]):
                self.player1.round_win()
            elif self.player1.choice == self.options[3] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[4]):
                self.player1.round_win()
            elif self.player1.choice == self.options[4] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[0]):
                self.player1.round_win()
            elif self.player2.choice == self.options[0] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[3]):
                self.player2.round_win()
            elif self.player2.choice == self.options[1] and (self.player1.choice == self.options[0] or self.player1.choice == self.options[4]):
                self.player2.round_win()
            elif self.player2.choice == self.options[2] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[3]):
                self.player2.round_win()
            elif self.player2.choice == self.options[3] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[4]):
                self.player2.round_win()
            elif self.player2.choice == self.options[4] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[0]):
                self.player2.round_win()        
                
    def display_winner(self):
        if self.player1.rounds_won == 2:
            print(f"{self.player1.name} has endured the onslaught of RPSLS and has beaten {self.player2.name}!!\n{self.player1.name} wins {self.player1.rounds_won} rounds to {self.player2.rounds_won}.")
        elif self.player2.rounds_won == 2:
            print(f"{self.player2.name} has endured the onslaught of RPSLS and has beaten {self.player1.name}!!\n{self.player2.name} wins {self.player2.rounds_won} rounds to {self.player1.rounds_won}.")


