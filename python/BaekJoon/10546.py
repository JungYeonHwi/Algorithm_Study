import sys
input= sys.stdin.readline

N = int(input())
arr = dict()
for _ in range(N):
    name = input().rstrip()
    if name not in arr.keys() : 
        arr[name] = 1
    else : 
        arr[name] += 1

for _ in range(N-1):
    name = input().rstrip()
    if name in arr.keys() : 
        arr[name] += 1

for key, values in arr.items() :
    if values %2 == 1 : 
        print(key)
        break