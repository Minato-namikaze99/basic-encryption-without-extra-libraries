import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters #this is a variable with all the characters, digits and punctutations with the space character too
#we didn't use string.whitespace because in that there are multiple types of whitespaces in it, like the escape characters too, which is like too much. So we just simply added the space character


chars = list(chars)
key = chars.copy()

random.shuffle(key) #shuffles the key list

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")