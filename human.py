from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        i = 0
        for gesture in self.options:
            i += 1
            print(f'\n{i}{gesture}')
        chosen_gesture = input('Please choose a gesture from the list. Please enter one of the corresponding numbers')
        chosen_gesture = int(chosen_gesture) - 1
        if chosen_gesture > -1 and chosen_gesture < 5:
            self.choice = self.options[chosen_gesture]
            print(f"\n {self.name} has chosen {self.choice}.\n")

    def set_name(self):
        self.name = input("Please enter your name here: ")
        








    # def player_choice(self, name):
    #     return super().player_choice(name)

    # def gesture_choice(self):
    #     return super().gesture_choice()