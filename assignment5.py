import hashlib

# Function to calculate SHA-1 hash
def calculate_sha1_hash(message):
    # Create a new sha1 hash object
    sha1_hash = hashlib.sha1()

    # Update the hash object with the message (encoded in bytes)
    sha1_hash.update(message.encode())

    # Get the hexadecimal representation of the SHA-1 hash
    hash_value = sha1_hash.hexdigest()

    return hash_value

# Example message to be transmitted
message = "test message for SHA-1 hash."

# Calculate SHA-1 hash
hash_value = calculate_sha1_hash(message)

# Display the original message and its SHA-1 hash
print("Original Message: ", message)
print("SHA-1 Hash: ", hash_value)

# Simulating message transmission and verification
received_message = message  # In a real scenario, the message would be received via network
received_hash = calculate_sha1_hash(received_message)

# Verifying message integrity using the SHA-1 hash
if hash_value == received_hash:
    print("\nMessage integrity verified. The message has not been altered.")
else:
    print("\nMessage integrity failed. The message has been altered.")
