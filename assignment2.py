import random
import time
from sympy import isprime

# Function to generate a random prime number
def generate_prime(bits):
    while True:
        # Generate a random number of the given bit size
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Function to compute the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse using Extended Euclidean Algorithm
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA Key Generation
def generate_rsa_keypair(bits):
    # Step 1: Generate two distinct prime numbers p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:  # Ensure p and q are distinct
        q = generate_prime(bits)
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute the totient (phi(n)) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Common choice for e
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    
    # Step 5: Compute d, the modular inverse of e modulo phi(n)
    d = modinv(e, phi_n)
    
    # Public key (e, n), Private key (d, n)
    return ((e, n), (d, n))

# RSA Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert plaintext to integers (using ord to get the ASCII value of characters)
    message = [ord(char) for char in plaintext]
    # Encrypt each character
    ciphertext = [pow(char, e, n) for char in message]
    return ciphertext

# RSA Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Decrypt each character
    decrypted_message = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_message)

# Main function to run the experiment with timing
def main():
    bits = 8  # Smaller bit size for testing; for stronger security, use 1024 or 2048 bits
    # Measure key generation time
    start_time = time.time()
    public_key, private_key = generate_rsa_keypair(bits)
    key_generation_time = time.time() - start_time
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = "hello"
    print(f"Original Message: {message}")
    
    # Measure encryption time
    start_time = time.time()
    ciphertext = encrypt(public_key, message)
    encryption_time = time.time() - start_time
    print(f"Encrypted Message: {ciphertext}")
    
    # Measure decryption time
    start_time = time.time()
    decrypted_message = decrypt(private_key, ciphertext)
    decryption_time = time.time() - start_time
    print(f"Decrypted Message: {decrypted_message}")
    
    # Print the times
    print(f"Key Generation Time: {key_generation_time:.6f} seconds")
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    print(f"Decryption Time: {decryption_time:.6f} seconds")

if __name__ == "__main__":
    main()
