"""
Write a function, check_palindrome() to check whether the given string is a palindrome or not.
The function should return true if it is a palindrome else it should return false.
"""

def check_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
