from collections import defaultdict

# Read input
n, m = map(int, input().split())
group_a = defaultdict(list)

# Populate group A with words and their indices
for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

# Process group B
for _ in range(m):
    word = input()
    if word in group_a:
        print(" ".join(map(str, group_a[word])))
    else:
        print(-1)
