#  type() a function that tells you what type of class a number you pass through is
print(type (2)) # output >> class 'int'
print(type (2.5)) # output >> class 'float'
print(type (2 + 2.5)) # output >> class 'float'
# Whenever doing math with both floats and ints, the result is a float. Otherwise, we would potentially lose any of our data after the decimal point.

# Division always returns a float in python
print(6/2) # output >> 3.0
print(type (6/2)) # output >> class 'float'

# When dividing use two "/" (i.e. //) if you want python to only return an int (by FLOORING (not rounding) answer)
print(10//7) # output >> 1
print(6//2) # output >> 3
print(type (6//2)) # output >> class 'int'

# ** is used to raise a number (exponents)
print(2 ** 3) # output >> 8 (2^3 or 2 raised to 3rd)

