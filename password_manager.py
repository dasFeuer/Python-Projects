from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Generating new key...")
        write_key()
        return load_key()

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|") 
                print(f"User: {user} and Password: {fer.decrypt(passw.encode()).decode()}")
    except FileNotFoundError:
        print("Password file not found.")

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing one (view, add), press `q` to quit?: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue



# from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
        

# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key


# key = load_key()
# fer = Fernet(key)

# def view():
#     with open('password.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|") 
#             print(f"User: {user} and Password: {(fer.decrypt(passw.encode()).decode)}")

# def add():
#     name = input('Account name: ')
#     pwd = input('Password: ')

#     with open('password.txt', 'a') as f:
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# while True:
#     mode = input("Would you like to add a new password or view existing one (view, add), press `q` to quit?: ").lower()
#     if mode == "q":
#         break

#     if mode == "view":
#         view()

#     elif mode == "add":
#         add()

#     else:
#         print("Invalid mode.")
#         continue