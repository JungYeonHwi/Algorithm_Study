from itertools import combinations

n = int(input())
arr = []

for i in range(n) :
    one = list(map(int, input().split()))
    arr.append(one)

data = [i for i in range(0, n)]

result = list(combinations(data, n // 2))
answer = []

for i in range(len(result)) : 
    tmxkxm = list(result[i])
    fldzm = []
    
    for j in data : 
        if j not in tmxkxm : 
            fldzm.append(j)
    
    tmxkxmValue = 0
    fldzmValue = 0
    
    for a in tmxkxm : 
        for b in tmxkxm : 
            tmxkxmValue += arr[a][b]
            
    for a in fldzm : 
        for b in fldzm : 
            fldzmValue += arr[a][b]
        
    answer.append(abs(tmxkxmValue - fldzmValue))
    
print(min(answer))