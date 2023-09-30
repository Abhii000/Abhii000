import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

# Input
test_cases = int(input())
for _ in range(test_cases):
    regex_string = input()
    result = is_valid_regex(regex_string)
    print(result)
