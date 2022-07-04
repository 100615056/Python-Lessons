import random
import string

# choice
# Return a random element from the non-empty sequence

# sample
# To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.

# join
#  The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.

# Randomly choose characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
text = ''
L_char = 5
U_char = 3
for char in range(L_char):
    text += random.choice(lower)
for chars in range(U_char):
    text += random.choice(upper)

# Shuffle the order of the characters and return a string value using join()
print('Original Text:', text)
shuffled_text = random.sample(text, len(text))
print('Shuffled Text:',shuffled_text)
joined_text = ''.join(shuffled_text)
print('Joined Text:', joined_text)
