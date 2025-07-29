import random

# List of characters to choose from
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

# Combine all characters
all_chars = letters + letters.upper() + numbers + symbols

# Ask user for password length
length = int(input("Enter password length: "))

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_chars)

# Show result
print("Your password is:", password)
