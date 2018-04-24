# test cases:
# cubeChecker(56.3, 1) --> false
# cubeChecker(-1, 2) --> false
# cubeChecker(8, 3) --> false
# cubeChecker(8, 2) --> true
# cubeChecker(-8,-2) --> false
# cubeChecker(0, 0) --> false
# cubeChecker(1, 5) --> false
# cubeChecker(125, 5) --> true
# cubeChecker(125,-5) --> false

def cube_checker(volume, side):
    if volume <= 0 or side <= 0: return False
    return volume % side == 0
    
