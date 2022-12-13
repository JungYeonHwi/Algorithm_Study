N = int(input())

students = []

for student_index in range(N) : 
    info = list(map(int, input().split(' ')))
    
    students.append(info)
    
students.sort(key=lambda student: student[2], reverse=True)

gold = students[0]
silver = students[1]
bronze = None

for i in range(2, len(students)) :
    if gold[0] == silver[0] == students[i][0] : continue
    else :
        bronze = students[i]
        break

print(gold[0], gold[1])
print(silver[0], silver[1])
print(bronze[0], bronze[1])