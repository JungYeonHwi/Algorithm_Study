a, c, e = map(int, input().split())
student = list(map(int, input().split()))
    
if (student[0] >= a and student[1] >= c and student[2] >= e) : print("A")
elif(student[0] >= a / 2 and student[1] >= c and student[2] >= e) : print("B")
elif(student[1] >= c and student[2] >= e) : print("C")
elif(student[1] >= c / 2 and student[2] >= e / 2) : print("D")
else : print("E")