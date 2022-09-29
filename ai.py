import random
from player import Player
class AI(Player):
    def __init__(self):
        super().__init__()


    def player_type(self):
        self.choice = random.choice(self.options)
        print(f"\nAI has chosen {self.choice}\n")

    def set_name(self):
        ai_names = ['Omega', 'Zero', 'Machina', 'Apex', 'Flux']
        self.name = random.choice(ai_names)
        

    # def player_choice(self, name):
    #     return super().player_choice(name)

    # def gesture_choice(self):
    #     return super().gesture_choice()
