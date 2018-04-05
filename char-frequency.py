# test cases:
#charFreq("I like cats") --> {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}


def char_freq(message):
    answer = {}
    for char in message:
        if char not in answer.keys():
            answer.update({char:1})
        else:
            answer[char] += 1
    return answer
