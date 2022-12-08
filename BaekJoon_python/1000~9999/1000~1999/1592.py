N, M, L = map(int, input().split())
arr = [0] * N
cnt = i = 0

while arr[i] < M-1 :
    arr[i] += 1
    cnt += 1
    if arr[i] % 2 == 1 : i = (i+L) % N  
    else : i = (i-L) % N
    
print(cnt)