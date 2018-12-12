from Door import Door

class WoodenDoor(Door):
    def __init__(self, fixed):
        super().__init__(fixed)
    
    def get_description(self):
        print ("This is a Wooden Door. Is it fixed: ", self.fixed)