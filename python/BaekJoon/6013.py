import math

def dist(a, b, c, d) : 
    return math.sqrt((a - c) ** 2) + math.sqrt((b-d) ** 2)

arr = []
n = int(input())

for _ in range(n) : 
    a, b = map(int, input().split())
    arr.append([a, b])
    
answer = []
    
for i in range(n) : 
    for j in range(i+1, n) : 
        value = dist(arr[i][0], arr[i][1], arr[j][0], arr[j][1])
        answer.append([i, j, value])
        
answer.sort(key = lambda x : -x[2])

print(answer[0][0]+1, answer[0][1]+1)