# Import libraries
from random import choice, sample
import string


def password_rules():
    # Ask for password requirements 
    while True:
        number = input('Provide number of passwords (positive integer): ')
        if not number.isnumeric():
            print('Enter valid number')
            continue

        length = input('Provide password length (positive integer): ')
        if not length.isnumeric():
            print('Enter valid length')
            continue

        lower = input('Provide minimum number of lowercase letters (positive integer): ')
        if not lower.isnumeric():
            print('Enter valid number for lowercase')
            continue

        upper = input('Provide minimum number of uppercase letters (positive integer): ')
        if not upper.isnumeric():
            print('Enter valid number for uppercase')
            continue

        digit = input('Provide minimum number of digits (positive integer): ')
        if not digit.isnumeric():
            print('Enter valid number for digits')
            continue

        special = input('Provide minimum number of special characters (positive integer): ') 
        if not special.isnumeric():
            print('Enter valid number for special characters')
            continue
            
        else:
            number = int(number)
            length = int(length)
            lower = int(lower)
            upper = int(upper)
            digit = int(digit)
            special = int(special)
            return number, length, lower, upper, digit, special

def get_password(requirements):
    number = requirements[0]
    length = requirements[1]
    lower = requirements[2]
    upper = requirements[3]
    special = requirements[4]
    digits = requirements[5]
    remaining = length - lower - upper - special - digits
    
    # Generate the selected number of passwords and store in list
    password_list = []
    for i in range(number):
        # Create password with the selected requirements
        password = ''
        for j in range(lower):
            password += choice(string.ascii_lowercase)
        for k in range(upper):
            password += choice(string.ascii_uppercase)
        for l in range(special):
            password += choice(string.punctuation)
        for m in range(digits):
            password += choice(string.digits)
        for n in range(remaining):
            password += choice(string.ascii_letters)
        
        # Shuffle password
        final_password = ''.join(sample(password, len(password)))
        password_list.append(final_password)
    
    return password_list


def main():
    # Store password requirements
    requirements = []
    passwords = []
    requirements = password_rules()
    passwords = get_password(requirements)

    
main()
