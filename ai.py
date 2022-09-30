import random
from player import Player
class AI(Player):
    def __init__(self):
        super().__init__()



    def set_name(self):
        ai_names = ['Omega', 'Zero', 'Machina', 'Apex', 'Flux']
        self.name = random.choice(ai_names)
        
    def choose_gesture(self):
        self.choice = random.choice(self.options)
        print(f"\n{self.name} has chosen {self.choice}\n")
        return self.choice