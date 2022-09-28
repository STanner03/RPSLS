from enterprise import Enterprise

class Match:
    def __init__(self):
    # , name_1, name_2):
        self.player1_name = ''
        self.player2_name = ''

    def play_round(self):
        Enterprise.gesture_list(self)
        Enterprise.player_choice(self)