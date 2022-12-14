n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
value = []

for i in range(1, n+1) : 
    value.append(arr[i-1])
    
    if len(value) == k : 
        answer.append(sum(value))
        del value[0]
        
print(max(answer))