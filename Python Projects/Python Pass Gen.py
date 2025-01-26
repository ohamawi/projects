#this is a password generator project
import random

print("This is a password generator".center(40,'='))
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

password_amount = int(input('How many passwords would you like? '))

length = int(input('How many characters would you like your password to be? '))

print('\nHere are the passwords!')

for pwd in range(password_amount):
    passwords = ''
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)