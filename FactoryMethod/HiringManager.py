from Interviewer import Interviewer

class HiringManager:
    def __init__(self):
        pass

    def make_interviewer(self):
        return Interviewer()
    
    def take_interview(self):
        interviewer = self.make_interviewer()
        interviewer.ask_questions()