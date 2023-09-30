from collections import Counter

# Read the input string
company_name = input().strip()

# Calculate the frequency of each character
char_count = Counter(company_name)

# Sort the characters by frequency (in descending order) and then by alphabetical order
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

# Print the top three characters and their occurrence counts
for char, count in sorted_chars[:3]:
    print(char, count)

'''x=str(input())
list1=list(x)
s=set(list1)
dict1={}
print(list1)
print(s)

for k in s:
    if list1.count(k)==1:
        continue
    print(k,list1.count(k))
    dict1[k]=list1.count(k)
print(dict1)
#sort dict with values
dict1=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
print(dict1)
for k,v in dict1:
    print(k,v)
    
'''