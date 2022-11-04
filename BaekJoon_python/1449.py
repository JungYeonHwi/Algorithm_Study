n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

tape = 1
dist = 0

for i in range(1, n) : 
    dist += abs(arr[i] - arr[i-1])
    
    if l > dist : 
        continue
    else : 
        tape += 1
        dist = 0

print(tape)
