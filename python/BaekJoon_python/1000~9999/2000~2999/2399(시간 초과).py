import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
answer = 0

for i in range(0, len(arr)) : 
    for j in range(i, len(arr)) : 
        answer += abs(arr[i] - arr[j])
        
print(answer * 2)