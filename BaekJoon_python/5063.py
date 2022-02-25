N = int(input())

for i in range(N) : 
    r, e, c = map(int, input().split())
    if (r + c == e) : print("does not matter")
    elif (e > r + c) : print("advertise")
    else : print("do not advertise")