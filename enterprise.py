import random

class Enterprise:
    def __init__(self):
        pass

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
        
    def game_round(self, option_1, option_2, option_3):
        pass

        
