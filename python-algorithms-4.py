# test cases
# name = "Santa Claus" and password = "Ho Ho Ho!" returns True
# name = "Chris Roper" and password = "Ho Ho!" returns False
# name = "Santa!" and password = "Ho Ho Ho!" returns False

class Sleigh(object):
    def authenticate(self, name, password):
        if name == "Santa Claus" and password == "Ho Ho Ho!":
            return True
        return False
    
