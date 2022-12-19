for _ in range(int(input())) : 
    n = int(input())
    answer = 0
    
    for i in range(n) : 
        s, a, b = map(str, input().split())
        a = int(a)
        b = float(b)
        
        answer += a * b

    print(f"${answer:.2f}")