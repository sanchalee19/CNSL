import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user(users_db):
    username = input("Enter username: ")
    if username in users_db:
        print("Username already exists! Please try again.")
        return
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    users_db[username] = hashed_password
    print("User registered successfully!")

# Function to login a user
def login_user(users_db):
    username = input("Enter username: ")
    if username not in users_db:
        print("Username does not exist! Please register first.")
        return
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    if users_db[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid password! Please try again.")

# Main function
def main():
    users_db = {}  # Dictionary to store username and hashed passwords

    while True:
        print("\n--- Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
