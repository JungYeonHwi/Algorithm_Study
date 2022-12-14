for _ in range(int(input())) : 
    A, B, C, D, E = map(int, input().split())
    answer = A * 350.34 + B * 230.90 + C * 190.55 + D * 125.30 + E * 180.90
    
    print("$" + "{:.2f}".format(answer))