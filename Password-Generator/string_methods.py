import string

# Displaying output for string methods
lower = string.ascii_lowercase
upper = string.ascii_uppercase
special = string.punctuation
digits = string.digits
remaining = string.ascii_letters

strings = {'Lowercase:':lower, 'Uppercase:':upper, 'Special:':special, 'Digits:':digits, 'All:':remaining}

for key, value in strings.items():
    print(key, value)
