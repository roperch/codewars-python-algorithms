# test cases:
# toFreud("") --> ""
# toFreud("") --> ""
# toFreud("test") --> "sex"
# toFreud("This is a test") --> "sex sex sex sex" 
# toFreud("This is a longer test") --> "sex sex sex sex sex" 
# toFreud("You're becoming a true freudian expert") --> "sex sex sex sex sex sex" 

def to_freud(sentence):
    answerArray = []
    sentence = sentence.split(' ')
    for i in range(len(sentence)):
        answerArray.append("sex")
    return ' '.join(answerArray)
