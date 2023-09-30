n = int(input())
nums = input().split()
print(all(int(num) > 0 for num in nums) and any(num == num[::-1] for num in nums))
