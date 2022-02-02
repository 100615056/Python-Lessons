# Print Function Properties
# Use a for loop or a while loop

# Lesson
# For Loop
# 1st way - List 
groceries = ['apple', 'orange', 'grape']
# 1) variable - index - keep track of your position in the list
for item in groceries:
  print(item)

#2nd way - Variable
#range (start, stop, step)
for i in range(10):
print(i)

# Challenge
#Print two rows of ? with 4 ? each
# 1st While Loop
#i = 0
while i < 2:
  print("????")
  i += 1
# 2nd for loop
for j in range(2):
  print('????')
  
# 3rd for loop
for i in range(2):
  for k in range(4):
    print("?", end = "")
  print()
