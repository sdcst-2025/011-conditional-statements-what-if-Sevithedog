#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
a = float(input("Enter a variable"))
b = float(input("Enter a variable"))
c = float(input("Enter a variable"))
if a > b and a> c:
    h = a
    l1 = b
    l2 = c
elif b > a and b > c:
    h = b
    l1 = a
    l2 = c
elif c > a and c > b:
    h = c
    l1 = a
    l2 = b
#print(f"{h},{l1},{l2}")
lower = h-(h*0.02)
upper = h+(h*0.02)
value = l1**2 + l2**2
#print(f"{lower},{value},{upper}")
if lower**2 < value < upper**2:
    print("That is a right triangle")
elif value > h**2:
    print("That is an obtuse triangle")
elif value < h**2:
    print("That is an acute triangle")
