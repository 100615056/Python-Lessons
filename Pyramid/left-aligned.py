# Print left-aligned pyramid given valid user input

# Validate user-input
def pyramid_height():
  while True:
    # Get Number
    number = int(input("Enter Number: "))
    # Check that number is within range
    if number >= 1 and number <= 8:
      break
  return number

# Print left-aligned pyramid
def print_pyramid(number):
  for i in range(number):
    for j in range(i + 1):
      print('#', end='')
    print()

def main():
  number = pyramid_height()
  print_pyramid(number)

main()
