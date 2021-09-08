import random

print("Welcome To Your Password Generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

try:
    num_of_pass = int(input("Amount of Password(s) to generate: "))
    length_of_pass = int(input("Password length: "))
except ValueError:
    print('Invalid Value')
    exit()
print("\nHere are/is your password(s):")


def generator():
    for pwd in range(num_of_pass):
        passwords = ""
        for c in range(length_of_pass):
            passwords += random.choice(chars)
        print(passwords)
    print("Be sure to save the passwords")
