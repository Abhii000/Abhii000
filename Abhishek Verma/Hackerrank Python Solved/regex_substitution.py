import re

# Read the integer n
n = int(input())

# Initialize an empty list to store the modified text
modified_text = []

# Loop through the next n lines of input
for _ in range(n):
    line = input()  # Read each line of text
    # Use regular expressions to replace '&&' and '||' with spaces on both sides
    modified_line = re.sub(r'(?<= )&&(?= )', 'and', line)
    modified_line = re.sub(r'(?<= )\|\|(?= )', 'or', modified_line)
    modified_text.append(modified_line)

# Print the modified text
for line in modified_text:
    print(line)
