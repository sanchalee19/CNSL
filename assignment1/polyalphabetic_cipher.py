def generate_shifts(key):
    return [ord(char.lower()) - ord('a') for char in key]

def encrypt(plaintext, key):
    shifts = generate_shifts(key)
    result = []
    key_length = len(shifts)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = shifts[i % key_length] 
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def decrypt(ciphertext, key):
    shifts = generate_shifts(key)
    result = []
    key_length = len(shifts)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = shifts[i % key_length]
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

# Example usage
plaintext = "HELLO WORLD"
key = "abc"

ciphertext = encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_text}")
