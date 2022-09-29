from player import Player
class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def choose_gesture(self):
        i = 0
        for gesture in self.options:
            i += 1
            print(f'{i}{gesture}')
        chosen_gesture = input('Please choose a gesture from the list')
        chosen_gesture = int(chosen_gesture) - 1
        self.choice = self.options[chosen_gesture]


    # def player_choice(self, name):
    #     return super().player_choice(name)

    # def gesture_choice(self):
    #     return super().gesture_choice()