#test cases
# 1 -> [1]
# 2 -> [1,2]
# 3 -> [1,2,3]

def create_array(n):
    res=[]
    i=0
    while i!=n: 
        i+=1
        res.append(i)
    return res
