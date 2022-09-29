class Player:
    def __init__(self, name):
        self.name = name
        self.rounds_won = 0
        self.choice = ''
        self.options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        
    def choose_gesture(self):
        pass
    # def player_choice(self, name):
    #     choice = input(f'\n{name} what do you choose? \nA) Rock \nB) Paper \nC) Scissors \nD) Lizard \nE) Spock \nPlease select A, B, C, D, or E:  ')
    #     while True:
    #         if choice == 'A' or choice == 'a':
    #             choice = self.options[0]
    #         elif choice == 'B' or choice == 'b':
    #             choice = self.options[1]
    #         elif choice == 'C' or choice == 'c':
    #             choice = self.options[2]
    #         elif choice == 'D' or choice == 'd':
    #             choice = self.options[3]
    #         elif choice == 'E' or choice == 'e':
    #             choice = self.options[4]
    #         if choice in self.options:
    #             print(f"\n{name} has chosen {choice}\n")
    #             return choice
    #         else:    
    #             choice = input('Invalid choice, please try again. \nA) Rock \nB) Paper \nC) Scissors \nD) Lizard \nE) Spock \nPlease select A, B, C, D, or E:  ')
    
    

    # def gesture_choice(self):
    #     self.player1.choice = self.player_choice(self.player1.name)
    #     self.player2.choice = self.player_choice(self.player2.name)
    #     if self.player1.choice == self.options[0] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[3]):
    #         self.player1.rounds_won += 1
    #     elif self.player1.choice == self.options[1] and (self.player2.choice == self.options[0] or self.player2.choice == self.options[4]):
    #         self.player1.rounds_won += 1
    #     elif self.player1.choice == self.options[2] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[3]):
    #         self.player1.rounds_won += 1
    #     elif self.player1.choice == self.options[3] and (self.player2.choice == self.options[1] or self.player2.choice == self.options[4]):
    #         self.player1.rounds_won += 1
    #     elif self.player1.choice == self.options[4] and (self.player2.choice == self.options[2] or self.player2.choice == self.options[0]):
    #         self.player1.rounds_won += 1
    #     elif self.player2.choice == self.options[0] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[3]):
    #         self.player2.rounds_won += 1
    #     elif self.player2.choice == self.options[1] and (self.player1.choice == self.options[0] or self.player1.choice == self.options[4]):
    #         self.player2.rounds_won += 1
    #     elif self.player2.choice == self.options[2] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[3]):
    #         self.player2.rounds_won += 1
    #     elif self.player2.choice == self.options[3] and (self.player1.choice == self.options[1] or self.player1.choice == self.options[4]):
    #         self.player2.rounds_won += 1
    #     elif self.player2.choice == self.options[4] and (self.player1.choice == self.options[2] or self.player1.choice == self.options[0]):
    #         self.player2.rounds_won += 1        