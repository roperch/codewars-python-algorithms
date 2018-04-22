# test cases:
# calculate_tip(30, "poor") --> 2
# calculate_tip(20, "Excellent") --> 4
# calculate_tip(20, "hi") --> 'Rating not recognised'
# calculate_tip(107.65, "GReat") --> 17
# calculate_tip(20, "great!") --> 'Rating not recognised'


import math
def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == "terrible":
        return math.ceil(amount * 0)
    elif rating == "poor":
        return math.ceil(amount * 0.05)
    elif rating == "good":
        return math.ceil(amount * 0.1)
    elif rating == "great":
        return math.ceil(amount * 0.15)
    elif rating == "excellent":
        return math.ceil(amount * 0.2)
    else:
        return "Rating not recognised"
