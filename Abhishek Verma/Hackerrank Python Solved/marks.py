import time,os
os.system('clear')
#make a program that print second lowest number is given input number
name=[]
marks=[]
dict={}
for a in range(int(input("enter the number of element:"))):
    
    name.append(str(input("Name = :"))) 
    marks.append(str(input("marks = :")))

    dict[marks[a]]=name[a]

print(dict)

sorted_list = sorted(dict.items(),reverse=True)

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print(sorted_dict)

original_dict = sorted_dict

reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)
newlist=[]
for key,value in reversed_dict.items():
    newlist.append(key)

newlist.remove(newlist[-1])
last_value=newlist[-1]
print(last_value)
second_lowest = reversed_dict.get(last_value)
print(second_lowest)



#corrected
if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))
