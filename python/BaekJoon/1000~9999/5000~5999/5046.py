n, b, h, w = map(int, input().split())
m = b + 1

for i in range(h) : 
    p = int(input())
    answer = []
    
    arr = list(map(int, input().split()))
    
    for idx in range(len(arr)) : 
        if arr[idx] >= n and n * p <= b : answer.append(n * p)

if len(answer) == 0 : print("stay home")
else : print(min(answer))