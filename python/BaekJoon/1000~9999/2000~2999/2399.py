import sys
 
n = int(sys.stdin.readline().rstrip())
arr = sys.stdin.readline().rstrip().split(' ')
prefixsum = []
 
for i in range(n) :
    arr[i] = int(arr[i])
    prefixsum.append(0)
 
arr.sort()
 
for i in range(1, n) :
    prefixsum[i] = prefixsum[i - 1] + (arr[i] - arr[i - 1]) * i
 
answer = 0
for i in prefixsum : answer += i
 
print(answer * 2)
 
