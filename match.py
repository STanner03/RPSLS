import random
from human import Human
from ai import AI

class Match:
    def __init__(self):
        self.player1 = Human()
        self.player2 = ""
        self.options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        
    def run_game(self):
        self.game_type()
        self.display_welcome()
        self.play_round()
        self.display_winner()
        self.credits()

    def display_welcome(self):
        print(f"\n                   {self.player1.name}       VS       {self.player2.name}")
        print("        *------------------------------------------------*")
        print("         Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("        *------------------------------------------------*")
        print("           ####                                    ####            ")
        print("         #########                              #########          ")
        print("         ##########                            ##########          ")
        print("          ##########                          ##########           ")
        print("           ##########                        ##########            ")
        print("     #####  ##########                      ##########  #####      ")
        print("   ######### ##########                    ########## #########    ")
        print("   ########## ##########                  ########## ##########    ")
        print("    ########## ##########                ########## ##########     ")
        print("     ########## ##########              ########## ##########      ")
        print("      ########## ##########            ########## ##########       ")
        print("       ########## ##########          ########## ##########        ")
        print("        ########## ##########        ########## ##########         ")
        print("         ########## ##########      ########## ##########          ")
        print("          ########## ##########    ########## ##########           ")
        print("           #####################  #####################            ")
        print("            ###########################################            ")
        print("            ## The Rules of the game are as follows: ##            ")
        print("            #######                              ######            ")
        print("            ###### Rock beats Scissors & Lizard!  #####            ")
        print("            ######   Paper beats Rock & Spock!    #####            ")
        print("            ###### Scissors beats Paper & Lizard! #####            ")
        print("            ######  Lizard beats Spock & Paper!   #####            ")
        print("            ######  Spock beats Rock & Scissors!  #####            ")
        print("            ########                            #######            ")
        print("            ###########################################            ")
        print("            ###########################################            ")
        print("            ###########################################            ")
        print("              #######################################              ")
        print("                  ###############################                  ")
        print("\nWhen either a Player or the AI wins a best 2 out of 3 rounds, they are the winners!")
        
    def play_round(self):
        while self.player1.rounds_won < 2 and self.player2.rounds_won < 2:
            print(f"\n{self.player1.name} has {self.player1.rounds_won} wins!\n{self.player2.name} has {self.player2.rounds_won} wins!\n")
            self.player1.choice = self.player1.choose_gesture()
            self.player2.choice = self.player2.choose_gesture()
            if self.player1.choice == self.options[0] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[3]):
                self.player1.round_win()
                if self.player2.choice == self.options[2]:
                    print('Rock crushes Scissors!')
                elif self.player2.choice == self.options[3]:
                    print('Rock crushes Lizard!')
            elif self.player1.choice == self.options[1] and (self.player2.choice == self.options[0] or self.player2.choice == self.options[4]):
                self.player1.round_win()
                if self.player2.choice == self.options[0]:
                    print('Paper covers Rock!')
                elif self.player2.choice == self.options[4]:
                    print('Paper disproves Spock!')
            elif self.player1.choice == self.options[2] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[3]):
                self.player1.round_win()
                if self.player2.choice == self.options[1]:
                    print('Scissors cuts Paper!')
                elif self.player2.choice == self.options[3]:
                    print('Scissors decapitates Lizard!')
            elif self.player1.choice == self.options[3] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[4]):
                self.player1.round_win()
                if self.player2.choice == self.options[1]:
                    print('Lizard eats Paper!')
                elif self.player2.choice == self.options[4]:
                    print('Lizard poisons Spock!')
            elif self.player1.choice == self.options[4] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[0]):
                self.player1.round_win()
                if self.player2.choice == self.options[2]:
                    print('Spock smashes Scissors!')
                elif self.player2.choice == self.options[0]:
                    print('Spock vaporizes Rock!')
            elif self.player2.choice == self.options[0] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[3]):
                self.player2.round_win()
                if self.player1.choice == self.options[2]:
                    print('Rock crushes Scissors!')
                elif self.player1.choice == self.options[3]:
                    print('Rock crushes Lizard!')
            elif self.player2.choice == self.options[1] and (self.player1.choice == self.options[0] or self.player1.choice == self.options[4]):
                self.player2.round_win()
                if self.player1.choice == self.options[0]:
                    print('Paper covers Rock!')
                elif self.player1.choice == self.options[4]:
                    print('Paper disproves Spock!')
            elif self.player2.choice == self.options[2] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[3]):
                self.player2.round_win()
                if self.player1.choice == self.options[1]:
                    print('Scissors cuts Paper!')
                elif self.player1.choice == self.options[3]:
                    print('Scissors decapitates Lizard!')
            elif self.player2.choice == self.options[3] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[4]):
                self.player2.round_win()
                if self.player1.choice == self.options[1]:
                    print('Lizard eats Paper!')
                elif self.player1.choice == self.options[4]:
                    print('Lizard poisons Spock!')
            elif self.player2.choice == self.options[4] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[0]):
                self.player2.round_win()
                if self.player1.choice == self.options[2]:
                    print('Spock smashes Scissors!')
                elif self.player1.choice == self.options[0]:
                    print('Spock vaporizes Rock!')        
                
    def display_winner(self):
        if self.player1.rounds_won == 2:
            print(f"\n{self.player1.name} has endured the onslaught of RPSLS and has beaten {self.player2.name}!!\n{self.player1.name} wins {self.player1.rounds_won} rounds to {self.player2.rounds_won}.")
        elif self.player2.rounds_won == 2:
            print(f"\n{self.player2.name} has endured the onslaught of RPSLS and has beaten {self.player1.name}!!\n{self.player2.name} wins {self.player2.rounds_won} rounds to {self.player1.rounds_won}.")

    def game_type(self):
        while True:
            answer = input("\nWould you like to play single-player against AI or multiplayer agsint another player?\nPlease select A) for AI or P) for Player: ")
            if answer == 'P' or answer == 'p':
                self.player2 = Human()
                break
            elif answer == 'A' or answer == 'a':
                print('\nYou will be playing single player mode against AI!')
                self.player2 = AI()
                break
            else:
                print("That was an invalid choice, please try again.\n")
        
    def credits(self):
        print("\n###############################################################")
        print("# *-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-* #")
        print("# Thank you for playing Rock, Paper, Scissors, Lizard, Spock! #")
        print("# *-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-`-_-* #")
        print("###############################################################\n")
        print("\nCo-Creators: Armando Beltran and Shane Tanner\n\nWe thank you for your time, and hope that you have enjoyed playing as much as we enjoyed co-creating!\n")
        play_again = input("Would you like to play again? Please enter Y for Yes or N for No\n")
        if play_again == 'y' or play_again == 'Y':
            self.player1.rounds_won = 0
            self.player2.rounds_won = 0
            self.run_game()
        else:
            pass