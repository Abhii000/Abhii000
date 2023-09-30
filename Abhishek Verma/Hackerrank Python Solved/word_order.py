from collections import OrderedDict

# Read the integer n
n = int(input())

# Create an empty OrderedDict to store word occurrences
word_count = OrderedDict()

# Read and process the words
for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Output the number of distinct words
print(len(word_count))

# Output the number of occurrences for each distinct word
print(*word_count.values())
