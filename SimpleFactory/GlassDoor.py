from Door import Door

class GlassDoor(Door):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.type = "Glass"
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def get_type(self):
        return self.type