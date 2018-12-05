from HiringManager import HiringManager
from CommunityExecutive import CommunityExecutive

class MarketingManager(HiringManager):
    def __init__(self):
        pass
    
    def make_interviewer(self):
        return CommunityExecutive()