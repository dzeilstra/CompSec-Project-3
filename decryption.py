import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms


# Read .txt file as a .txt file in Python
# Read it line by line and strip all of the newline characters
# .rstrip()
msg = open("encrypted2.txt", "r", encoding="ANSI")
list1 = list()
for x in msg:
    print(x.rstrip())
    list1.append(x.rstrip())

complete = list1[0]+list1[1]
print(complete)

#print(list)

words = open("wordsEn.txt", "r")
list2 = list()
for word in words:
    if len(word) == 16:
        word = word.rstrip()
    if len(word) < 16:
        word = word.rstrip()
        word = word.ljust(16)
    if len(word) > 16:
        word = word.rstrip()
        word = word[:16]
    list2.append(word)

print(list2)
print(len(list2))

for word in list2:
    # Then pad them out if they are less than 16 chars and truncate if longer
    # Then once padded satisfactorily, use .encode() to convert the string object into a byte string
    # Then I can use it as a key

    #complete = complete.encode()

    key = word.encode()
    iv = b"0"*16
    cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    # Read the encrypted file as a binary using RB mode (how to read a Python file in binary)
    
    with open('encrypted2.txt', 'rb') as file:
        bin_data = file.read()

    #print(bin_data)

    result = decryptor.update(bin_data) + decryptor.finalize()
    #result = result.decode('ANSI')
    
    if b"the" in result:
        print(result)
        print(word)
        print(key)
    
    #with open("output.txt", "w") as decrypted:
    #    decrypted.write(result)