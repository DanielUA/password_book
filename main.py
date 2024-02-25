from cryptography.fernet import Fernet
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)
def view():
    with open("password.txt", mode="r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", mode="a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("What would you like to add a new pass or view, q for exit")

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    
    else:
        print("Invalid mode.")
        continue