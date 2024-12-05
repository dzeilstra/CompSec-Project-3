import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms



for i in range(109583):
    # Read .txt file as a .txt file
    # Read it line by line and strip all of the newline characters
    # .rstrip()

    # Then pad them out if they are less than 16 chars and truncate if longer
    # Then once padded satisfactorily, use .encode() to convert the string object into a byte string
    # Then I can use it as a key
    key = "PLACEHOLDER"
    iv = b"0"*16
    cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    # Read the encrypted file as a binary using RB mode (how to read a Python file in binary)
    result = decryptor.update("PLACEHOLDER") + decryptor.finalize()
    print(result)

    # Test