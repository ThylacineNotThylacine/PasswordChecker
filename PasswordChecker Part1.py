"""
Password Checker Part 1 - Assignment to see whether the password has both numbers and letters. Second attempt so have
commented out sections not needed, i.e. convert from part2

Name: Mitchell Evans, Date 13.09.21, Assignment PasswordChecker2
"""
# Pseudocode
# Program      - Password checker part 1
# Inputs       - Password
#
# Calculations - isalpha & isnumeric ( only letters used and only numbers )
#

# While    - calculation - isalpha
#          - Output - weak password txt
#          - Input -  password
#
# While    - calculation - isnumeric
#          - Output - weak password txt
#          - Input -  password
#
# OUTPUT   - strong password text

# Name to identify who created the program
print("PasswordChecker1 program developed by Mitchell Evans")
# I wanted a line break as I feel it's easier to read when you are running the program choosing to go for empty print.
print("")
# Inputs - Initial password input, this is looped later on if users are unsuccessful in creating a strong password.
#        - This variable can be changed multiple times within the program
password = input("Enter your password here: ")

"""
THIS SECTION COMMENTED OUT AS NOT APPLICABLE HERE
# Constants - Setting the validation of password length through the two constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

# password length variable is used in the first validation step and while loop and can be changed at each while loop
passwordLength = len(password)


This while loop is the first while loop and is used to see whether the password fits the conditions > min password 
length and < max password length. From there the loop will print your password length -> weak password and the needed 
characters to pass through this validation step. The loop continues by asking too input the password again, changing the 
password variable, from there -> it calculates the new password length to see whether T or F to loop conditions.

while passwordLength < MIN_PASSWORD_LENGTH or passwordLength > MAX_PASSWORD_LENGTH:
    print("Your password is", passwordLength, "characters, Password weak - password must be between 6 - 10 characters")
    password = input("Please enter password again: ")
    passwordLength = len(password)
"""

# This while loop is used to calculate if the password only has letters, if true users asked to change password
while password.isalpha():
    print("Password weak - contains only letters")
    password = input("Please enter password again: ")

# This while loop is used to calculate if the password only has numbers, if true users asked to change password
while password.isnumeric():
    print("Password weak - contains only numbers")
    password = input("Please enter password again: ")

# Final output of a strong password, unsure whether password length should be removed?
print("Your password is - Password strong")
