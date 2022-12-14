T = int(input())

for _ in range(T) : 
    N, D = map(int, input().split())
    
    result = 0
    
    for j in range(N) :
        v, f, c = map(int, input().split())
        if f / c * v >= D : result += 1
    print(result)