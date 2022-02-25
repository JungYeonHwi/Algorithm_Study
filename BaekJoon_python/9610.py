N = int(input())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(N) : 
    A, B = map(int, input().split())
    
    if (A == 0 or B == 0) : AXIS += 1
    elif (A > 0 and B > 0) : Q1 += 1
    elif (A < 0 and B > 0) : Q2 += 1
    elif (A < 0 and B < 0) : Q3 += 1
    elif (A > 0 and B < 0) : Q4 += 1
    
print("Q1:" , Q1)
print("Q2:" , Q2)
print("Q3:" , Q3)
print("Q4:" , Q4)
print("AXIS:" , AXIS)