from DoorFactory import DoorFactory

door1 = DoorFactory.make_wooden_door(10, 50)
print(door1.get_height(), door1.get_width(), door1.get_type())

door2 = DoorFactory.make_glass_door(100, 200)
print (door2.get_height(), door2.get_width(), door2.get_type())