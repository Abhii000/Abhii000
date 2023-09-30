

dict={}

for loop in range(int(input('type = '))):
    name=[]
    score=[]
                    

    list1=[]
    for a in range(1):
        x=input("Enter: ").split(' ')
        list1=list(x)
        print(list1)
    for i in list1:
        if i.isdigit():
            score.append(int(i))
        else:
            name.append(i)
    dict[f'{name[0]}']=f'{sum(score)/len(score)}'
get_marks=dict.get(f'{input("Enter the Student name to get avg: ")}')
print(get_marks)


        
