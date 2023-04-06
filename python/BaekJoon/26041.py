A = list(input().split())
B = input()
cnt = 0

for i in range(len(A)) :
    if A[i] == B :	
        continue	
    else :
        if A[i][:len(B)] == B :
            cnt += 1
print(cnt)