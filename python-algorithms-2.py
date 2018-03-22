#test cases
#solution("1", "22") # returns "1221"
#solution("22", "1") # returns "1221"

def solution(a, b):
    if len(a)>len(b):
        return "{}{}{}".format(b,a,b)
    elif len(a)<len(b):
        return "{}{}{}".format(a,b,a)
