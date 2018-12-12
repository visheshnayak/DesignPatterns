from FittingExpert import FittingExpert
from WoodenDoor import WoodenDoor

class Carpenter(FittingExpert):
    def __init__(self):
        pass
    
    def get_description(self):
        print ("I can fix a wooden door.")
    
    def fix_door(self, WoodenDoor):
        WoodenDoor.fixed = True
        print ("Fixed wooden door.")