# Function to generate the first N Fibonacci numbers
def generate_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    return fibonacci

# Input
n = int(input())

# Generate the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)

# Use map and lambda to cube each number
cubed_fibonacci = list(map(lambda x: x**3, fibonacci_numbers))

# Output the result
print(cubed_fibonacci)
