from FittingExpert import FittingExpert
from IronDoor import IronDoor

class Welder(FittingExpert):
    def __init__(self):
        pass
    
    def get_description(self):
        print ("I can fix iron doors.")
    
    def fix_door(self, IronDoor):
        IronDoor.fixed = True
        print ("Fixed Iron door.")