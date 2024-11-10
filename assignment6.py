from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import hashlib

# Step 1: Generate RSA keys (for X and Y)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Step 2: Encrypt message using recipient's public key
def encrypt_message(message, recipient_public_key):
    key = RSA.import_key(recipient_public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Step 3: Decrypt message using private key
def decrypt_message(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Step 4: Create a digital signature
def sign_message(message, private_key):
    key = RSA.import_key(private_key)
    hash_obj = SHA256.new(message.encode())
    signer = pkcs1_15.new(key)
    signature = signer.sign(hash_obj)
    return signature

# Step 5: Verify the digital signature
def verify_signature(message, signature, public_key):
    key = RSA.import_key(public_key)
    hash_obj = SHA256.new(message.encode())
    verifier = pkcs1_15.new(key)
    try:
        verifier.verify(hash_obj, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")

# Step 6: Hash the message for integrity check
def hash_message(message):
    hash_obj = SHA256.new(message.encode())
    return hash_obj.hexdigest()

# Example usage
if __name__ == '__main__':
    # Generate keys for X and Y
    X_private_key, X_public_key = generate_rsa_keys()
    Y_private_key, Y_public_key = generate_rsa_keys()
    
    # X wants to send a message to Y
    original_message = "Hello, Y. This is a confidential message."

    # Step 1: Encrypt the message using Y's public key
    encrypted_message = encrypt_message(original_message, Y_public_key)

    # Step 2: X signs the message for non-repudiation
    signature = sign_message(original_message, X_private_key)

    # Step 3: Y receives the encrypted message, decrypts it and verifies the signature
    decrypted_message = decrypt_message(encrypted_message, Y_private_key)

    print(f"Decrypted Message: {decrypted_message}")

    # Step 4: Verify the signature to ensure non-repudiation
    verify_signature(decrypted_message, signature, X_public_key)

    # Step 5: Check the message integrity
    message_hash = hash_message(decrypted_message)
    print(f"Message Hash: {message_hash}")
