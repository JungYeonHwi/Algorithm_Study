for _ in range(int(input())) : 
    a, b = map(float, input().split())
    
    h = a * 2 / b
    print(f"The height of the triangle is {h:.2f} units")