# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:36:54 2024

@author: PMLS
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    if length <= 0:
        print("Please enter a valid length greater than 0.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
