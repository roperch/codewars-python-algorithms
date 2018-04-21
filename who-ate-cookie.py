# test cases:
# cookie("Ryan") --> "Who ate the last cookie? It was Zach!"
# cookie(26) --> "Who ate the last cookie? It was Monica!"
# cookie(2.3) --> "Who ate the last cookie? It was Monica!"
# cookie(true) --> "Who ate the last cookie? It was the dog!"



def cookie(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) is float:
        return "Who ate the last cookie? It was Monica!"
    elif type(x) is int:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
