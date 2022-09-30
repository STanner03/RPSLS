from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()


    def set_name(self):
        self.name = input("\nPlease enter Player's name here: ")
        

    def choose_gesture(self):
        i = 0
        for gesture in self.options:
            i += 1
            print(f'\n{i}) {gesture}')
        while True:
            chosen_gesture = input(f'\n{self.name}, please choose a gesture from the list. Please enter one of the corresponding numbers! ')
            if chosen_gesture == '1' or chosen_gesture == '2' or chosen_gesture == '3' or chosen_gesture == '4' or chosen_gesture == '5':
                chosen_gesture = int(chosen_gesture) - 1
                if chosen_gesture > -1 and chosen_gesture < 5:
                    self.choice = self.options[chosen_gesture]
                    print(f"\n{self.name} has chosen {self.choice}.\n")
                    return self.choice