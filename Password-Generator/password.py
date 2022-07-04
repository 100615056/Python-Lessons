# Import libraries
from random import choice, sample
import string

# Cryptography
from cryptocode import encrypt, decrypt
from cryptography.fernet import Fernet
import rsa


def password_rules():
    # Ask for password requirements
    while True:
        number = input('Provide number of passwords (positive integer): ')
        if not number.isnumeric():
            continue

        length = input('Provide password length (positive integer): ')
        if not length.isnumeric():
            continue

        lower = input(
            'Provide minimum number of lowercase letters (positive integer): ')
        if not lower.isnumeric():
            continue

        upper = input(
            'Provide minimum number of uppercase letters (positive integer): ')
        if not upper.isnumeric():
            continue

        digit = input('Provide minimum number of digits (positive integer): ')
        if not digit.isnumeric():
            continue

        special = input(
            'Provide minimum number of special characters (positive integer): ')
        if not special.isnumeric():
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
    encrypt_message = encrypt(message, key)
    return encrypt_message


def decrypt_cryptocode(message, key):
    decrypt_message = decrypt(message, key)
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

# Cryptography Package (Fernet)
def encrypt_fernet(message, fernet):
    encrypt = fernet.encrypt(message.encode())
    return encrypt


def decrypt_fernet(message, fernet):
    decrypt = fernet.decrypt(message).decode()
    return decrypt


def apply_fernet_encrypt(passwords, fernet):
    encrypt_message = []
    for entry in passwords:
        encrypt = encrypt_fernet(entry, fernet)
        encrypt_message.append(encrypt)
    return encrypt_message


def apply_fernet_decrypt(encryption, fernet):
    decrypt_message = []
    for entry in encryption:
        decrypt = decrypt_fernet(entry, fernet)
        decrypt_message.append(decrypt)
    return decrypt_message

# RSA Algorithm
def encrypt_rsa(message, publickey):
    encrypt = rsa.encrypt(message.encode(), publickey)
    return encrypt


def decrypt_rsa(message, privatekey):
    decrypt = rsa.decrypt(message, privatekey).decode()
    return decrypt


def apply_rsa_encrypt(passwords, publickey):
    encrypt_message = []
    for entry in passwords:
        encrypt = encrypt_rsa(entry, publickey)
        encrypt_message.append(encrypt)
    return encrypt_message


def apply_rsa_decrypt(encryption, privatekey):
    decrypt_message = []
    for entry in encryption:
        decrypt = decrypt_rsa(entry, privatekey)
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
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encryption = apply_fernet_encrypt(passwords, fernet)
        result = apply_fernet_decrypt(encryption, fernet)
    if selection == 3:
        publickey, privatekey = rsa.newkeys(512)
        encryption = apply_rsa_encrypt(passwords, publickey)
        result = apply_rsa_decrypt(encryption, privatekey)

    
main()
