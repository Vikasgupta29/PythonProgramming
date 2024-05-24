"""
Write a python program to display all the common characters between two strings.
Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
Sample Input:
"I like Python"
"Java is a very popular language"
Expected output:
lieyon
"""

def find_common_characters(msg1,msg2):
    common_characters=""
    for i in msg1:
        if i in msg2 and i not in common_characters:
            common_characters+=i
    if len(common_characters)==0:
        common_characters=-1
    return common_characters

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
