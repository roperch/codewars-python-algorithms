# test cases:
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi!!"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"

def remove(s):
    if s=="":return ""
    if s[-1] == "!":
        return s[0:-1]
    return s
    
