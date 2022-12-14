def f(K, prime) :
    for i in prime :
        for j in prime :
            for k in prime :
                if i+j+k == K :
                    print(i, j, k)
                    return ;
    print(0)

arr = [1] * 1001
for i in range(2, int(1000**0.5)+1) :
    if arr[i] :
        for j in range(i+i, 1001, i) :
            arr[j] = 0
prime = [i for i in range(2, 1001) if arr[i]]

for _ in range(int(input())) :
    K = int(input())
    f(K, prime)