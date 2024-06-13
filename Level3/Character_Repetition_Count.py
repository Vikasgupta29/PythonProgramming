"""
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding.
Repetition of character has to be replaced by storing the length of that run.
Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
Provide different String values and test your program.
Sample Input -> AABCCA
Expected Output -> 2A1B2C1A
"""

def encode(message):
    encoded_message=""
    t_char=""
    t_count=""
    count=0
    for i in message:
        count+=1
        if i==t_char:
            t_count+=1
        else:
            encoded_message+=(str(t_count)+t_char)
            t_char=i
            t_count=1
    encoded_message+=(str(t_count)+t_char)
    return encoded_message

encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
