# test cases:
# startingMark(1.52) --> 9.45
# startingMark(1.83) --> 10.67
# startingMark(1.22) --> 8.27
# startingMark(2.13) --> 11.85

def starting_mark(height):
    m = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - (m*1.83)
    return round(m*height+c,2)
