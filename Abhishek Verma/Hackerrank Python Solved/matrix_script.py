import re

def decode_matrix_script(rows, columns, matrix):
    # Combine the characters in the columns
    encoded_script = ''.join(matrix[i][j] for j in range(columns) for i in range(rows))
    
    # Use regular expression to replace symbols or spaces between alphanumeric characters
    decoded_script = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', encoded_script)
    
    return decoded_script

# Input
rows, columns = map(int, input().split())
matrix = [input() for _ in range(rows)]

# Decode and print the script
decoded_script = decode_matrix_script(rows, columns, matrix)
print(decoded_script)
