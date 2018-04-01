# test cases
# symmetricPoint([0,0], [1,1]) --> [2, 2]
# symmetricPoint([2, 6], [-2, -6]) --> [-6, -18]
# symmetricPoint([10, -10], [-10, 10]) --> [-30, 30]
# symmetricPoint([1, -35], [-12, 1]) --> [-25, 37]
# symmetricPoint([1000, 15], [-7, -214]) --> [-1014, -443]
# symmetricPoint([0, 0], [0, 0]) --> [0, 0]


def symmetric_point(p, q):
    return [(q[0]-p[0])+q[0],(q[1]-p[1])+q[1]]
