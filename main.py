def caesar_encrypt(plain):
    cipher = ''
    for character in plain:
        if (character == ' '):
            cipher += ' '
        else:
            cipher += (chr(ord(character) + shift))
    return cipher

def caesar_decrypt(cipher):
    decipher = ''
    for character in cipher:
        if (character == ' '):
            decipher += ' '
        else:
            decipher += (chr(ord(character) - shift))
    return decipher

shift = 3

plain = 'Caesar Cipher'
encrypt = caesar_encrypt(plain)
print(encrypt)
print(plain)

message = input("Enter a message to encrypt: ")
encryptedMessage = caesar_encrypt(message)
print(encryptedMessage)
