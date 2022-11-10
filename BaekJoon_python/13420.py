for _ in range(int(input())) :
    arr = input().split()
    a, b, c = int(arr[0]), int(arr[2]), int(arr[4])
    op = arr[1]
    
    if op == '+' : t = a+b
    elif op == '-' : t = a-b
    elif op == '*' : t = a*b
    elif op == '/' : t = a//b
    if t == c : print("correct")
    else : print("wrong answer")