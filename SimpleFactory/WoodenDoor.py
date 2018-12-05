from Door import Door

class WoodenDoor(Door):
    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.type = "Wooden"
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def get_type(self):
        return self.type