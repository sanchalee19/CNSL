def caesar_cipher(plain_text, shift):
    result = []

    for char in plain_text:
        if char.isupper():
            result.append(chr((ord(char) + shift - 65) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) + shift - 97) % 26 + 97))
        else:
            result.append(char)
    
    return ''.join(result)

plain_text = input("Enter plain text: ")
shift = int(input("Enter shift: "))

encrypted_text = caesar_cipher(plain_text, shift)
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, -shift)
print(f"Decrypted: {decrypted_text}")
