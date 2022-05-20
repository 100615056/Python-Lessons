# Reading Files - Method 1
file = open('test.txt')
for line in file:
    print(line, end='')
print()
file.close()

# Reading Files - Method 2
with open('test.txt', 'r') as file:
    print(file.read())

# Writing to Files
with open('write.txt', 'w') as file:
    file.write('Testing out writing to files\n')
    file.write('Seems to work\n')
    file.write('Finished')

# Counting lines in a file
with open('write.txt', 'r') as file:
    content = file.readlines()
    
count = 0
for line in content:
    count += 1
print(count)
    
