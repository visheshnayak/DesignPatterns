from Door import Door

class IronDoor(Door):
    def __init__(self, fixed):
        super().__init__(fixed)

    def get_description(self):
        print ("This is an Iron Door. Is it fixed: ", self.fixed)