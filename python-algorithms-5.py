#test cases:
# uniTotal("a") == 97 
# uniTotal("aaa") == 291
# uniTotal ("c") == 99
# uniTotal ("b") == 98

def uni_total(string):
    ascii_total = 0
    for char in string:
        ascii_total += ord(char)
    return ascii_total
