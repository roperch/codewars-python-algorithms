

def is_uppercase(inp):
    if inp=="0":return False
    for char in inp:
        if ord(char) >= 97 and ord(char) <= 122:
            return False
    return True
