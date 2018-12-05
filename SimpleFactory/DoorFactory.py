from WoodenDoor import WoodenDoor
from GlassDoor import GlassDoor

class DoorFactory:
    @staticmethod
    def make_wooden_door(width, height):
        return WoodenDoor(height, width)
    
    @staticmethod
    def make_glass_door(width, height):
        return GlassDoor(height, width)