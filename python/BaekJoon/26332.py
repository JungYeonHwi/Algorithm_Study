for _ in range(int(input())) : 
    a, b = map(int, input().split())
    print(a, b)
    value = a - 1
    
    answer = a * b - value * 2
    print(answer)