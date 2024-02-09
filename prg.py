# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# Following are the criteria for checking the password:
# ○ At least 1 letter between [a-z]
# ○ At least 1 number between [0-9]
# ○ At least 1 letter between [A-Z]
# ○ At least 1 character from [$#@]
# ○ Minimum length of transaction password: 6
# ○ Maximum length of transaction password: 12
import re


def validate_password(user_input):
    f = re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,12}$", user_input)
    if f:
        return user_input

    return "None"


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5
# are to be printed in a comma-separated sequence.
# Example:
# Input : 0100,0011,1010,1001
# Output: 1010

def binary_digits(input_string_list):
    items = []
    num = [x for x in input_string_list.split(',')]
    for p in num:
        x = int(p, 2)
        print(x)
        if x % 5 == 0:
            items.append(p)
    print(','.join(items))


def main():
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(4)
    with open("file_password.txt", "r") as f:
        r = f.read()

    results = pool.map(validate_password, r.split(","))
    print(', '.join(results))


main()
