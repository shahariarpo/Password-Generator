master_pass = input("Master Password: ")


def view():
    pass


def add():
    name = input("Account name: ")
    password = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(name + " | " + password + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, press 'q' to quit)? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid input")
        continue
