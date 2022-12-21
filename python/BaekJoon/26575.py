for _ in range(int(input())) : 
    a, b, c = map(float, input().split())
    answer = a * b * c
    print(f"${answer:.2f}")