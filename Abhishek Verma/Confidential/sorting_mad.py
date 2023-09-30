'''x=str(input())
alpha=[]
digits=[]

arranged_alpha=[]

for a in x:
    if a.isalpha():
        alpha.append(a)
    else:
        digits.append(int(a))

arranged_alpha=sorted(alpha)
arranged_digit=sorted(digits)
for i in arranged_alpha:
    if i.isupper():
        arranged_alpha.remove(i)
        arranged_alpha.append(i)


for k in digits:
    if int(k)%2==0:
        arranged_digit.remove(k)
        arranged_digit.append(k)


for abhi in arranged_alpha:
    print(abhi,end="")
for verma in arranged_digit:
    print(verma,end="")'''

s = input()

# Sort the string using custom sorting criteria
sorted_s = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

# Join the sorted characters back into a string
result = ''.join(sorted_s)

print(result)
