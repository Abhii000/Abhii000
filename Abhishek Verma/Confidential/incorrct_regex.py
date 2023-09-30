import re

# Function to check if a regex is valid
def is_valid_regex(regex_str):
    try:
        re.compile(regex_str)
        return True
    except re.error:
        return False

# Input the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    regex_str = input().strip()
    try:
        re.compile(regex_str)
        print("True")
    except re.error:
        print("False")
