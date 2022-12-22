import sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())) : 
    arr.append(int(input()))
    
print(len(arr))
print(sum(arr))