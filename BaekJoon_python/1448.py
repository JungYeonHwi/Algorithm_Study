import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N) :
    arr.append(int(input()))

arr.sort(reverse=True)

res = 0
for i in range(len(arr) - 2) :
    if arr[i] < arr[i+1] + arr[i+2] :
        res = arr[i] + arr[i+1] + arr[i+2]
        break
    else :
        res = -1

print(res)