# test cases:
# isDigit("3") --> True
# isDigit("  3  ") --> True
# isDigit("-3.23") --> True
# isDigit("3-4") --> False
# isDigit("  3   5") --> False
# isDigit("3 5") --> False
# isDigit("zero") --> False

def isDigit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

