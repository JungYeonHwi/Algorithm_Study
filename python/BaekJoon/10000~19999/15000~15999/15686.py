from itertools import combinations

N, M = map(int, input().split())
arr = []
for _ in range(N) : 
    one = list(map(int, input().split()))
    arr.append(one)

home = []
chiken = []
    
for i in range(0, len(arr)) : 
    for j in range(len(arr[i])) : 
        if arr[i][j] == 1 : home.append([i+1, j+1])
        elif arr[i][j] == 2 : chiken.append([i+1, j+1])
        
result = 999999
        
for chi in combinations(chiken, M) : 
    temp = 0
    for h in home : 
        chikenLen = 999
        for j in range(M) :
            chikenLen = min(chikenLen, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chikenLen
    result = min(result, temp)

print(result)