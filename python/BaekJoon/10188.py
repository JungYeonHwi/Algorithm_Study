for _ in range(int(input())) : 
    a, b = map(int, input().split())
    for i in range(b) : 
        for j in range(a) : 
            print("X", end="")
        print()
    print()