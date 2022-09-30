class Player:
    def __init__(self):
        self.name = ""
        self.rounds_won = 0
        self.choice = ''
        self.options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.set_name()
        
    def set_name(self):
        pass
    
    def choose_gesture(self):
        pass

    def round_win(self):
        self.rounds_won += 1