import hashlib

#def generate_hash(password):
    # sha1 = hashlib.sha1()
    # sha1.update(message.encode('utf-8'))
    # return sha1.hexdigest()

def generate_hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()


def registerUser(userDB):
    username = input("Enter username: ")
    if username in userDB:
        print("Username already exists, try another username")
        return
    
    password = input("Enter password: ")
    hashPassword = generate_hash(password)
    userDB[username] = hashPassword 

    print("User registered successfully! ")


def loginUser(userDB):
    username = input("Enter username: ")
    if username not in userDB:
        print("Username does not exist. ")
        return
    
    password = input("Enter password: ")
    hashpassword = generate_hash(password)

    if userDB[username] == hashpassword:
        print("Login successful")
    else:
        print("Invalid password")


def main():
    userDB = {}

    while True: 
        print("---------login form---------")
        print("1. Register")
        print("2. Login")
        print("3. Exit ")

        choice = int(input("Enter choice: "))

        if choice == 1:
            registerUser(userDB)

        elif choice == 2:
            loginUser(userDB)

        elif choice == 3:
            return 
        
        else:
            print("Enter valid choice!")

if __name__ == "__main__":
    main()



