import random

# Function to perform the Diffie-Hellman key exchange
def diffie_hellman_key_exchange(prime, base, private_key):
    return pow(base, private_key, prime)

# Simulate the Man-in-the-Middle attack
def mitm_attack(prime, base, alice_private, bob_private):
    # Step 1: Alice sends her public key to Eve (MITM)
    alice_public = diffie_hellman_key_exchange(prime, base, alice_private)

    # Step 2: Eve intercepts Alice's public key and sends her own public key to Bob
    eve_private = random.randint(1, prime-1)  # Eve's private key
    eve_public = diffie_hellman_key_exchange(prime, base, eve_private)

    # Bob receives Eve's public key, not Alice's
    # Step 3: Eve intercepts Bob's public key and sends her own public key to Alice
    bob_public = diffie_hellman_key_exchange(prime, base, bob_private)

    # Step 4: Eve calculates the shared key with Alice and Bob separately
    shared_key_with_alice = diffie_hellman_key_exchange(prime, eve_public, alice_private)
    shared_key_with_bob = diffie_hellman_key_exchange(prime, eve_public, bob_private)

    print(f"Alice's public key: {alice_public}")
    print(f"Bob's public key: {bob_public}")
    print(f"Eve's public key: {eve_public}")
    print(f"Shared key between Alice and Eve: {shared_key_with_alice}")
    print(f"Shared key between Bob and Eve: {shared_key_with_bob}")
    
    return shared_key_with_alice, shared_key_with_bob

# Example values for Diffie-Hellman parameters
prime = 23  # A small prime number for simplicity
base = 5    # A primitive root modulo `prime`

# Private keys for Alice and Bob (randomly chosen)
alice_private = random.randint(1, prime-1)
bob_private = random.randint(1, prime-1)

# Perform the Man-In-The-Middle Attack
shared_key_with_alice, shared_key_with_bob = mitm_attack(prime, base, alice_private, bob_private)
