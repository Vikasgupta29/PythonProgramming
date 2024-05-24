"""
Write a python program that displays a message as follows for a given number:
1. If it is a multiple of three, display "Zip"
2. If it is a multiple of five, display "Zap".
3. If it is a multiple of both three and five, display "Zoom".
4. If it does not satisfy any of the above given conditions, display "Invalid".
"""

def display(num):
    if num%3==0 and num%5==0:
        message="Zoom"
    elif num%3==0:
        message="Zip"
    elif num%5==0:
        message="Zap"
    else:
        message="Invalid"
    return message

# Provide different values for num and test your program.
message=display(9)
print(message)
