# test cases:
# array('') --> None
# array('1') --> None
# array('1, 3') --> None
# array('1,2,3') --> '2'
# array('1,2,3,4') --> '2 3'


def array(string):
    string = string.split(",")
    if len(string) <= 2:
        return None
    del string[0]
    del string[-1]
    return " ".join(string)
