def can_stack_cubes(test_cases):
    results = []
    for cubes in test_cases:
        left = 0
        right = len(cubes) - 1
        prev_cube = float('inf')  # Initialize prev_cube to positive infinity
        
        while left <= right:
            if cubes[left] >= cubes[right] and cubes[left] <= prev_cube:
                prev_cube = cubes[left]
                left += 1
            elif cubes[right] > cubes[left] and cubes[right] <= prev_cube:
                prev_cube = cubes[right]
                right -= 1
            else:
                results.append("No")
                break
        else:
            results.append("Yes")
    
    return results

# Input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    test_cases.append(cubes)

# Check if it's possible to stack the cubes for each test case
results = can_stack_cubes(test_cases)

# Output results
for result in results:
    print(result)
