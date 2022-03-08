"""
1. Not operator and any()
2. for loops
3. items() method
4. Print methods - Oneline vs. Twoline
(Print vs Placeholder)
"""

# Not Operator - Boolean Logic - AND, OR, NOT
grades = ['Math', 'Science', 'English']
if not any(grades):
    print('Yes')
else:
    print('No')

# Different methods to print dictionary items using items() method, for loops, and placeholders
books = {"Harry Potter": 10, "Hunger Games": 8, "Percy Jackson": 7}

# Method 1 - One Line
for title, rating in books.items():
    print('Title:', title, end=' | ')
    print('Rating:', rating)

# Method 2 - One Line
for title, rating in books.items():
    print(f'Title: {title} | Rating: {rating}')

# Method 1 - Two Line
for title, rating in books.items():
    print('Title:', title)
    print('Rating:', rating)

# Method 2 - Two Line
for title, rating in books.items():
    print(f'Title: {title}\nRating: {rating}')
    print(f'Title: {title}')
    print(f'Rating: {rating}')
