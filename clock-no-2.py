# test cases:
# past(0,1,1) --> 61000
# past(1,1,1) --> 3661000
# past(0,0,0) --> 0
# past(1,0,1) --> 3601000
# past(1,0,0) --> 3600000

def past(h, m, s):
    return ((h*60*60+m*60+s)*1000)
