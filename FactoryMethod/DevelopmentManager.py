from HiringManager import HiringManager
from Developer import Developer

class DevelopmentManager(HiringManager):
    def __init__(self):
        pass
    
    def make_interviewer(self):
        return Developer()