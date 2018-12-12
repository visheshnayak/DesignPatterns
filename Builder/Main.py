from BurgerBuilder import BurgerBuilder

#get the builder object
builder = BurgerBuilder("Large")

#build the burger
builder.add_cheese()
builder.add_lettuce()
builder.add_pepperoni()
builder.add_tomato()

#get the burger object
burger = builder.build_burger()

#get the burger description
burger.get_description()