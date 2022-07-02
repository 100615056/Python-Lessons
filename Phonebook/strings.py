"""
The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.

A numeric character has following properties:
Numeric_Type=Decimal
Numeric_Type=Digit
Numeric_Type=Numeric
"""

# isnumeric() method
a = '1234'
b = 'fdss43543'
c = '234fsdj'
d = 'fdhs'

# Store examples in a list 
examples = [a, b, c, d]

for item in examples:
    if item.isnumeric():
        print('All characters are numeric')
    else:
        print('All characters are not numeric')

# String methods for formating text
text = 'Harry POTTER and THE PRISONER of AZkaban'

# Convert to lowercase
print(text.lower()) 

# Convert to uppercase
print(text.upper())

# Convert 1st letter of each word in uppercase
print(text.title())
