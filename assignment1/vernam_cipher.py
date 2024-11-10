def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        print("Key must be the same length as the plaintext.")
    
    encrypted = []
    for i in range(len(plaintext)):
        encrypted_char = ord(plaintext[i]) ^ ord(key[i])
        encrypted.append(encrypted_char)
    
    return ''.join(format(char, '02x') for char in encrypted)

def vernam_decrypt(ciphertext, key):
    decrypted = []
    for i in range(0, len(ciphertext), 2):
        encrypted_char = int(ciphertext[i:i+2], 16)
        decrypted_char = chr(encrypted_char ^ ord(key[i//2]))
        decrypted.append(decrypted_char)
    
    return ''.join(decrypted)

plaintext = "HELLO"
key = "ABCDE"

ciphertext = vernam_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_text = vernam_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_text}")
