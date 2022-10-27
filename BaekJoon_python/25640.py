check = input()
n = int(input())

cnt = 0

for _ in range(n) : 
    arr = input()
    
    if arr == check : cnt += 1
    
print(cnt)