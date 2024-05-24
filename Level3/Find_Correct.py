"""
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.
And return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.
Sample Input -> {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
Expected Output -> [2, 2, 1]
"""

def find_correct(word_dict):
    correct,almost_correct,wrong=0,0,0
    for key,value in word_dict.items():
        if key==value:
            correct+=1
        elif len(key)!=len(value):
            wrong+=1
        else:
            t_count=0
            for x,y in zip(key,value):
                if x!=y:
                    t_count+=1
            if t_count>2:
                wrong+=1
            else:
                almost_correct+=1
    return [correct,almost_correct,wrong]
            
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
