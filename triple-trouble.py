triple_trouble("aaa","bbb","ccc") --> "abcabcabc"
triple_trouble("aaaaaa","bbbbbb","cccccc") --> "abcabcabcabcabcabc"
triple_trouble("burn", "reds", "roll") --> "brrueordlnsl"
triple_trouble("Bm", "aa", "tn") --> "Batman"
triple_trouble("LLh", "euo", "xtr") --> "LexLuthor"


def triple_trouble(one, two, three):
    answer = []
    one = list(one)
    two = list(two)
    three = list(three)
    for i in range(len(one)):
        answer.append(one[i])
        answer.append(two[i])
        answer.append(three[i])
    return ''.join(answer)
