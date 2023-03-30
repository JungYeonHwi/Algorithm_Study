N = int(input())
A = list(map(int, input().split()))
check = True	
shape = True 	

for i in range(N-1) :
    if A[i] < A[i+1] :
        if shape == False :	
            check = False
            break
    elif A[i] == A[i+1] :	
        check = False
        break
    else :
        shape = False

if check :
    print('YES')
else :
    print('NO')