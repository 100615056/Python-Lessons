# Create a double half-pyramid using hashes (#) where the user decides the height by entering a number between 1 and 8, inclusive.

def valid_pyramid():
  while True:
    # Get Number
    number = int(input("Enter Number: "))
    # Check that number is within range
    if number >= 1 and number <= 8:
      break
  return number

# Print pyrmaid
def print_pyramid(number, spaces):
  for i in range(number):
    for j in range(spaces):
      print('.', end='')
    for k in range(i + 1):
      print('#', end='')
    print('.', end='')
    for l in range(i+1):
      print('#', end='')
    print()
    spaces -= 1

# Right-aligned space for first row
def calculate_spaces(height):
  space = height
  return space


def main():
  height = valid_pyramid()
  spaces = calculate_spaces(height)
  print_pyramid(height, spaces)


main()
