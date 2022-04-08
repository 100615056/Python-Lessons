# Import libraries
from random import choice, sample
import string

# Cryptography
import cryptography
import cryptocode
from cryptography.fernet import Fernet


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


def cryptography_options():
    cryptography = ['Cryptocode', 'Cryptography Package', 'RSA Algorithm']
    for i, type in enumerate(cryptography):
        print(i+1, type)


def menu_selection():
    while True:
        cryptography_options()
        option = input('Choose Encryption Option: ')
        if option.isnumeric():
            choice = int(option)
            if choice >= 1 and choice <= 3:
                return choice
        else:
            continue


# Cryptocode 
def encrypt_cryptocode(message, key):
    encrypt_message = cryptocode.encrypt(message, key)
    return encrypt_message

def decrypt_cryptocode(message, key):
    decrypt_message = cryptocode.decrypt(message, key)
    return decrypt_message 

def apply_cryptocode_encrypt(passwords):
    encrypt_message = []
    key = input('Please enter cipher key: ')
    for entry in passwords:
        encrypt = encrypt_cryptocode(entry, key)
        encrypt_message.append(encrypt)
    return encrypt_message

def apply_cryptocode_decrypt(encryption):
    decrypt_message = []
    key = input('Please enter cipher key: ')
    for entry in encryption:
        decrypt = decrypt_cryptocode(entry, key)
        decrypt_message.append(decrypt)
    return decrypt_message


def store_encryption(encryption):
    # Store encryption in a text file
    with open('encrypt.txt', 'w') as f:
        # Add a newline after each element
        f.write('\n'.join(encryption))


def store_passwords(passwords):
    # Store passwords in a text file
    with open('pass.txt', 'w') as f:
        # Add a newline after each element
        f.write('\n'.join(passwords))


def main():
    # Store password requirements
    requirements = []
    passwords = []
    selection = menu_selection()
    requirements = password_rules()
    passwords = get_password(requirements)
    if selection == 1:
        encryption = apply_cryptocode_encrypt(passwords)
        result = apply_cryptocode_decrypt(encryption)
        if not any(result):
            print('Incorrect Key')
    if selection == 2:
        print('')


main()
