# 메모리 초과
from itertools import permutations

n = int(input())
inputCheck = list(map(int, input().split()))
idx = 0
data = []

for i in range(1, n+1) : 
    data.append(i)

result = list(permutations(data, n))
answerCheck = []

for i in range(0, len(result)) : 
    one = []
    for j in result[i] : 
        one.append(j)
        
    answerCheck.append(one)

for i in range(0, len(answerCheck)) : 
    if answerCheck[i] == inputCheck : idx = i

if idx == len(answerCheck) - 1 : print(-1)
else : 
    for i in answerCheck[idx+1] : 
        print(i, end= " ")
    