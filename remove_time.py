// test cases:
// shorten_to_date("Monday February 2, 8pm") --> "Monday February 2"
// shorten_to_date("Tuesday May 29, 8pm") --> "Tuesday May 29"
// shorten_to_date("Wed September 1, 3am") --> "Wed September 1"
// shorten_to_date("Friday May 2, 9am") --> "Friday May 2"
// shorten_to_date("Tuesday January 29, 10pm") --> "Tuesday January 29"

def shorten_to_date(long_date):
    return long_date.split(",")[0]
