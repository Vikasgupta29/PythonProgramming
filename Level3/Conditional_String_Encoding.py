"""
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.
Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately
If a word has only vowels then retain the word as is
If a word has a consonant (at least 1) then retain only those consonants
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Sample Input -> I love Python
Expected Output -> I lv Pythn
"""

def sms_encoding(data):
    e_data=[]
    vowel="aeiou"
    data=data.split()
    for word in data:
        t_word=""
        t_vowel=""
        for char in word:
            if char.lower() in vowel:
                t_vowel+=char
            else:
                t_word+=char
        if len(t_word)==0:
            e_data.append(t_vowel)
        else:
            e_data.append(t_word)
    encoded_data=" ".join(e_data)
    return encoded_data

data="I love Python"
print(sms_encoding(data))
