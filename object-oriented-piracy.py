# test cases
# Ship(15,10) --> 
# Ship(30,15) --> 
# Ship (45,20) --> 

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        if self.draft - self.crew * 1.5 > 20:
            return True
        return False
