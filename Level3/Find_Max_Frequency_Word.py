"""
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
Sample Input -> "Work like you do not need money love like you have never been hurt and dance like no one is watching"
Expected Output -> like 3
"""

def max_frequency_word_counter(data):
    frequency_dict={}
    data=data.lower().split()
    set_data=set(data)
    for word in set_data:
        frequency_dict[word]=data.count(word)
    d_max=max(frequency_dict.values())
    for key,value in frequency_dict.items():
        if value!=d_max:
            set_data.remove(key)
    word=max(set_data, key=len)
    frequency=frequency_dict[word]
    print(word,frequency)

data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
