# Using the cryptocode library
# pip install cryptocode
from cryptocode import encrypt, decrypt
message = 'Cryptography is fun'
cipher = 'bubbletea'

scrambled = encrypt(message, cipher)
print('Encryption:', scrambled)
decoded = decrypt(scrambled, cipher)
print('Decryption:', decoded)

# Using the cryptography package
from cryptography.fernet import Fernet

movie = 'Harry Potter and the Deathly Hallows'
Ferney key usage
key = Fernet.generate_key()
fernet = Fernet(key)
# Encryption
encoded = fernet.encrypt(movie.encode())
print('Encoded:', encoded)
decode = fernet.decrypt(encoded).decode()
print('Decoded:', decode)


# Using the RSA Algorithm
# pip install rsa
import rsa

publickey, privatekey = rsa.newkeys(512)
print('Pubkey:',publickey)
print('Privkey:', privatekey)
encrypt = rsa.encrypt(message.encode(), publickey)
print('En:', encrypt)
decrypt = rsa.decrypt(encrypt, privatekey).decode()
print('Dec:', decrypt)
