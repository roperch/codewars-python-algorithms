# test cases:
# pointsPer48(12, 20) --> 28.8
# pointsPer48(10, 10) --> 48.0
# pointsPer48(5, 17) --> 14.1
# pointsPer48(0, 0) --> 0
# pointsPer48(30.8, 34.7) --> 42.6
# pointsPer48(22.9, 33.8) --> 32.5

def nba_extrap(ppg, mpg):
    return round(ppg * (48 / mpg),1)
