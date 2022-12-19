for _ in range(int(input())) : 
    a, b = map(float, input().split())
    answer = abs(a-b)
    print(f"{answer:.1f}")