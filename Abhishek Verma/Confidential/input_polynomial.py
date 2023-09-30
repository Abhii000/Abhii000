cube = lambda x: x**3

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < n:
            next_number = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_number)
        return fibonacci

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
