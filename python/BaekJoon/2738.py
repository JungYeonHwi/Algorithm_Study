N, M = map(int, input().split())

A = []
B = []

answer = []

for i in range(N) :
    A.append(list(map(int, input().split())))
    
for i in range(N) :
    B.append(list(map(int, input().split())))
    
for i in range(N) : 
    arr = []
    for j in range(M) : 
        arr.append(A[i][j] + B[i][j])
        
    answer.append(arr)
    
for i in answer : 
    print(*i)