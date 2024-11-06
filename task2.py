#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

n = float(input("Enter a number"))
if n > 0:
    print("positive")
elif n == 0:
    print("zero")
elif n < 0:
    print("negative")