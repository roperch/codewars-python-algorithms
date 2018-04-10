# test cases:
# areYouPlayingBanjo("Martin") --> "Martin does not play banjo"
# areYouPlayingBanjo("Rikke") --> "Rikke plays banjo"

def areYouPlayingBanjo(name):
    if name[0] == 'r' or name[0] == 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
        
