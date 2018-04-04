# test cases
# isOpposite("ab","AB") --> true
# isOpposite("aB","Ab") --> true
# isOpposite("aBcd","AbCD") , true
# isOpposite("aBcde","AbCD") , false
# isOpposite("AB","Ab") , false
# isOpposite("","") , false

def is_opposite(s1,s2):
    if s1=="" or s2=="":return False
    for i in range(len(s1)):
        if abs(ord(s1[i]) - ord(s2[i])) != 32:
            return False
    return True
