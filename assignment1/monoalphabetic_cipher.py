import random
import string

def generate_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    key = dict(zip(alphabet, shuffled_alphabet))
    return key

def create_reverse_key(key):
    reverse_key = {v: k for k, v in key.items()}
    return reverse_key

def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            base = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            encrypted_message += key[char.lower()].upper() if char.isupper() else key[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(ciphertext, reverse_key):
    decrypted_message = ''
    for char in ciphertext:
        if char.isalpha():
            base = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            decrypted_message += reverse_key[char.lower()].upper() if char.isupper() else reverse_key[char]
        else:
            decrypted_message += char
    return decrypted_message

def main():
    key = generate_key()
    reverse_key = create_reverse_key(key)

    print("Generated Key:")
    for k, v in key.items():
        print(f"{k} -> {v}")
    
    while True:
        choice = input("Encrypt or decrypt? (e/d/x=exit): ").lower()
        if choice == 'e':
            plaintext = input("Enter the message to encrypt: ")
            encrypted = encrypt(plaintext, key)
            print("Encrypted message:", encrypted)
        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ")
            decrypted = decrypt(ciphertext, reverse_key)
            print("Decrypted message:", decrypted)
        elif choice == 'x':
            return
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
