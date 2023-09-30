'''list1=[]
for x in range(int(input())):
    n=int(input())
    
    if n<=33:
        print(n)
    else:
        k=n//10
    
        if n%10<5:
            
            round1=(k*10)+5
            
            if round1-n<3:
                
                print(round1)
            else:
                print(n)

        else:
            round2=(k*10)+10
            
            if round2-n<3:
                
                print(round2)
            else:
                print(n)
    
'''
def round_grades(num_students, grades):
    rounded_grades = []

    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple_5 = ((grade // 5) + 1) * 5
            if next_multiple_5 - grade < 3:
                rounded_grades.append(next_multiple_5)
            else:
                rounded_grades.append(grade)

    return rounded_grades

# Input
num_students = int(input())
grades = []
for _ in range(num_students):
    grade = int(input())
    grades.append(grade)

# Calculate rounded grades
rounded_grades = round_grades(num_students, grades)

# Output
for grade in rounded_grades:
    print(grade)
