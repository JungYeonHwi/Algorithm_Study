n = int(input())

for i in range(n) : 
    a, b, c, d = map(int, input().split())
    
    s = b + c + d

    if s < 55 : 
        p = f"{a} {s} FAIL"
        print(p)
    elif b / 35 < 0.3 : 
        p = f"{a} {s} FAIL"
        print(p)
    elif c / 25 < 0.3 : 
        p = f"{a} {s} FAIL"
        print(p)
    elif d / 40 < 0.3 : 
        p = f"{a} {s} FAIL"
        print(p)
    elif d / 40 >= 0.3 and c / 25 >= 0.3 and b / 35 >= 0.3 : 
        p = f"{a} {s} PASS"
        print(p)