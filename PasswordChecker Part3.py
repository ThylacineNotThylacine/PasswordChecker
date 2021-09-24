"""
Password Checker Part 3 - Assignment to create a password checker, that validates whether the password length is within
the require amount 6 - 10 along with checking to see whether the password has both numbers and letters. The password
checker now also writes to a file when an user inputs an incorrect password on the password length variables

Name: Mitchell Evans, Date 07.09.21, Assignment PasswordChecker3
"""
# Pseudocode
# Program      - Password checker part 3
# Inputs       - Password
# Constants    - Minimum password length 6 and Max length 10
#              - Password Log file
# Calculations - Password length
# Calculations - isalpha & isnumeric ( only letters used and only numbers )
#
# While    - Password length < min password length - Validation step
#          - Output - password length & weak password txt
#          - Input - password
#          - calculation - password length
#
# While    - Password length > max password length - Validation step
#          - Output - password length & weak password txt
#          - Input - password
#          - calculation - password length
#
# Output   - Logfile -> Datetime, password < 6 or >6
#
# While    - calculation - isalpha
#          - Output - password length & weak password txt
#          - Input -  password
#
# While    - calculation - isnumeric
#          - Output - password length & weak password txt
#          - Input -  password
#
# OUTPUT   - Password length & strong password text

import datetime


def main():
    print("PasswordChecker3 program developed by Mitchell Evans")
# I wanted a line break as I feel it's easier to read when you are running the program choosing to go for empty print.
    print("")


# Inputs - Initial password input, this is looped later on if users are unsuccessful in creating a strong password.
#        - This variable can be changed multiple times within the program
password = input("Enter your password here: ")
my_date = str(datetime.datetime.today())

# Constants - Setting the validation of password length through the two constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10
PASSWORD_LOG_FILE = "password_log_Mitchell_Evans.txt"

# password length variable is used in the first validation step and while loop and can be changed at each while loop

"""
This while loop is the first while loop and is used to see whether the password fits the conditions > min password. 
From there the loop will print your password length -> weak password and the needed 
characters to pass through this validation step. The loop continues by asking too input the password again, changing the 
password variable, from there -> it calculates the new password length to see whether T or F to loop conditions.
"""
passwordLength = len(password)

while passwordLength < MIN_PASSWORD_LENGTH:
    print("Your password is", passwordLength, "characters, Password weak - password must be between 6 - 10 characters")

    PASSWORD_LOG_FILE = open("password_log_Mitchell_Evans.txt", "a")
    # Once this while loop is opened the log file opened and it records the 'time' and a message '< 6' then closing
    PASSWORD_LOG_FILE.write(my_date)
    PASSWORD_LOG_FILE.write(", Password < 6")
    PASSWORD_LOG_FILE.write("\n")
    # log file closes to begin another loop or exit
    PASSWORD_LOG_FILE.close()

    password = input("Please enter password again: ")
    passwordLength = len(password)

while passwordLength > MAX_PASSWORD_LENGTH:
    print("Your password is", passwordLength, "characters, Password weak - password must be between 6 - 10 characters")

    PASSWORD_LOG_FILE = open("password_log_Mitchell_Evans.txt", "a")
    # Once this while loop is opened the log file is opened recording the 'time' and a message stating '> 10'
    PASSWORD_LOG_FILE.write(my_date)
    PASSWORD_LOG_FILE.write(", Password > 10 ")
    PASSWORD_LOG_FILE.write("\n")
    # log file closes to begin another loop or exit
    PASSWORD_LOG_FILE.close()

    password = input("Please enter password again: ")
    passwordLength = len(password)

PASSWORD_LOG_FILE = open("password_log_Mitchell_Evans.txt", "r")
# log file is printed on the screen through asking it to print each line before ending the task and closing the file,
# data in log file contains time and 6 or > 10 which was stated earlier on entry of data
for line in PASSWORD_LOG_FILE:
    print(line, end='')
PASSWORD_LOG_FILE.close()


# This while loop is used to calculate if the password only has letters, if true users asked to change password
# along with print of password length
while password.isalpha():
    print("Password contains", passwordLength, "characters", "- Password weak - contains only letters")
    password = input("Please enter password again: ")

# This while loop is used to calculate if the password only has numbers, if true users asked to change password
# along with print of password length
while password.isnumeric():
    print("Password contains", passwordLength, "characters", "- Password weak - contains only numbers")
    password = input("Please enter password again: ")


# Final output of a strong password, unsure whether password length should be removed?
print("Your password is", passwordLength, "characters - Password strong")
main()
