import re

def is_valid_uid(uid):
    # Check if it contains at least 2 uppercase English alphabet characters.
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False

    # Check if it contains at least 3 digits.
    if len(re.findall(r'\d', uid)) < 3:
        return False

    # Check if it contains only alphanumeric characters and has a length of 10 characters.
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False

    # Check if no character repeats.
    if len(set(uid)) != len(uid):
        return False

    return True

# Read the number of test cases.
t = int(input())

# Process each test case.
for _ in range(t):
    uid = input()
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")
