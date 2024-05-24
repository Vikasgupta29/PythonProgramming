"""
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. 
Otherwise returns False.
The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
Note: Perform case insensitive comparison wherever applicable.
"""

def check_anagram(data1,data2):
    if sorted(data1.lower())==sorted(data2.lower()):
        for x,y in zip(data1.lower(),data2.lower()):
            print(x,y)
            if x==y:
                return False
        return True
    else:
        return False
            
print(check_anagram("eat","tea"))
