N = int(input())
A = list(map(int,input().split()))

if N <= 2 :
    print(max(A))
else :
    res = [A[0], A[N - 1]]

    for i in range(1,len(A)-1) :
        res.append(A[i] + min(A[i+1], A[i-1]))

    print(max(res))