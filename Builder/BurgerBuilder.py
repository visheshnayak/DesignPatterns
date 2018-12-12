from Burger import Burger

class BurgerBuilder:
    def __init__(self, size):
        self.size = size
        self.pepperoni = False
        self.cheese = False
        self.lettuce = False
        self.tomato = False
    
    def add_pepperoni(self):
        self.pepperoni = True
    
    def add_cheese(self):
        self.cheese = True
    
    def add_lettuce(self):
        self.lettuce = True

    def add_tomato(self):
        self.tomato = True
    
    def build_burger(self):
        return Burger(self)