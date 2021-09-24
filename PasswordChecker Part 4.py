"""
Password Checker Part 4 - Assignment to create a password checker, that validates whether the password length is within
the require amount 6 - 10 along with checking to see whether the password has both numbers and letters. The password
Checker now validates a txt file turns it into a list, prints it on the screen and outlines the total errors and how
many times the user has put in the PW above or below the minimum character levels. - Section 3 has been commented out
to ensure easy readability. This can be placed back on if needed?

Name: Mitchell Evans, Date 13.09.21, Assignment PasswordChecker4
"""

# Pseudocode
# Program      - Password checker part 4
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
    print()


print("PasswordChecker4 program developed by Mitchell Evans")


# I wanted a line break as I feel it's easier to read when you are running the program choosing to go for empty print.
print("")

my_date = str(datetime.datetime.today())
log_data = []
count_pw_too_small = '<'
count_pw_too_large = '>'
letterCount = 0
# Inputs - Initial password input, this is looped later on if users are unsuccessful in creating a strong password.
#        - This variable can be changed multiple times within the program
password = input("Enter your password here: ")

# Constants - Setting the validation of password length through the two constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10
PASSWORD_LOG_FILE1 = "password_log_Mitchell_Evans.txt"
PASSWORD_LOG_FILE = "ITWorks_password_log.txt"

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
    password = input("Please enter password again: ")
    passwordLength = len(password)

"""    PASSWORD_LOG_FILE1 = open("password_log_Mitchell_Evans.txt", "a")
    # Once this while loop is opened the log file opened and it records the 'time' and a message '< 6' then closing
    PASSWORD_LOG_FILE1.write(my_date)
    PASSWORD_LOG_FILE1.write(", Password < 6")
    PASSWORD_LOG_FILE1.write("\n")
    # log file closes to begin another loop or exit
    PASSWORD_LOG_FILE1.close()

    password = input("Please enter password again: ")
    passwordLength = len(password)
"""
while passwordLength > MAX_PASSWORD_LENGTH:
    print("Your password is", passwordLength, "characters, Password weak - password must be between 6 - 10 characters")
    password = input("Please enter password again: ")
    passwordLength = len(password)

"""    PASSWORD_LOG_FILE1 = open("password_log_Mitchell_Evans.txt", "a")
    # Once this while loop is opened the log file is opened recording the 'time' and a message stating '> 10'
    PASSWORD_LOG_FILE1.write(my_date)
    PASSWORD_LOG_FILE1.write(", Password > 10 ")
    PASSWORD_LOG_FILE1.write("\n")
    # log file closes to begin another loop or exit
    PASSWORD_LOG_FILE1.close()

    password = input("Please enter password again: ")
    passwordLength = len(password)

PASSWORD_LOG_FILE1 = open("password_log_Mitchell_Evans.txt", "r")
# log file is printed on the screen through asking it to print each line before ending the task and closing the file,
# data in log file contains time and 6 or > 10 which was stated earlier on entry of data
for line in PASSWORD_LOG_FILE1:
    print(line, end='')
PASSWORD_LOG_FILE1.close()
"""

# This section is whereby I open the file and convert it to a list through appending, list name is now log_data
PASSWORD_LOG_FILE = open("ITWorks_password_log.txt", "r")
for line in PASSWORD_LOG_FILE:
    log_data.append(line)
PASSWORD_LOG_FILE.close()

# Printing out the entire list and calling the printout log_errors chosen a for list until no more lines
for log_errors in log_data:
    print(log_errors, end="")
print("")
print("")

# I wanted to give an overview of the total of errors before going into the pw too small or too large so that you can
# quickly validate whether you have all the errors in the list i.e. does it = 30
print(f"The total number of errors in the list are: {len(log_data):d}")
print("")

# Using a for loop and the LetterCount ability to seek the amount of times < has been used in the list, with the use of
# counting lines
for line in log_data:
    letterCount += line.count(count_pw_too_small)
print(f"The number of password attempts below the minimum are {letterCount} times")
print("")

# Had to reset my Letter count to zero or it will continue to count from the last for loop count interaction. In this
# way the total wont be 30 but start counting from 0 again.
letterCount = 0

# Using a for loop and the LetterCount ability to seek the amount of times > has been used in the list, with the use of
# counting lines
for line in log_data:
    letterCount += line.count(count_pw_too_large)
print(f"The number of password attempts above the maximum are {letterCount} times")
print("")

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
