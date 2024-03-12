# Importing Modules:
# string for string constants.
# random for random number generation.
import string
import random

# Password Generator Function:
# Generates a random password of specified length.
# Uses ASCII letters, digits, and punctuation.

def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password
# Password Generation Loop:
# Asks the user for password length.
# Validates input (positive integer).Generates and prints the password.  Asks if the user wants another password
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            continue

        generated_password = password_generator(length)
        print("Generated Password:", generated_password)

        continue_choice = input("Do you want to generate another password? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break
#     Handling Invalid Input:
#      Catches ValueError for invalid input.
#       Asks the user to enter a valid integer.
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
