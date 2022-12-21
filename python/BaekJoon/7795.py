for _ in range(int(input())) : 
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    count = 0
    pair = 0
 
    for i in range(n):
        while True:
            if count == m or a[i] <= b[count] :
                pair += count
                break
            else :
                count += 1
 
    print(pair)