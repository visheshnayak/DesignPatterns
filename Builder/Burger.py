class Burger:
    def __init__(self, BurgerBuilder):
        self.size = BurgerBuilder.size
        self.cheese = BurgerBuilder.cheese
        self.lettuce = BurgerBuilder.lettuce
        self.tomato = BurgerBuilder.tomato
        self.pepperoni = BurgerBuilder.pepperoni
    
    def get_description(self):
        print ("Burger description: ")
        print ("Size: ", self.size)
        print ("Cheese: ", self.cheese)
        print ("Lettuce: ", self.lettuce)
        print ("Tomato: ", self.tomato)
        print ("Pepperoni: ", self.pepperoni)