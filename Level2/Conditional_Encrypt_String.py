"""
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Sample Input -> the sun rises in the east
Expected Output -> eht snu sesir ni eht stea
"""

def encrypt_sentence(sentence):
    vowel="aeiou"
    encrypted_sentence=""
    sentence=sentence.split()
    for i in sentence:
        if (sentence.index(i)+1)%2!=0:
            encrypted_sentence+=i[::-1]
        else:
            t_word=""
            t_vowel=""
            for j in i:
                if j.lower() in vowel:
                    t_vowel+=j
                else:
                    t_word+=j
            encrypted_sentence+=(t_word+t_vowel)
        if i!=sentence[-1]:
            encrypted_sentence+=" "
                    
    return encrypted_sentence

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
