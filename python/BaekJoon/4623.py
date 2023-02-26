while 1:
    A, B, C, D = map(int, input().split())
    
    if A == B == C == D == 0 : break
    if A < B : A, B = B, A
    if C < D : C, D = D, C
    
    s, e = 1, 100

    while s <= e :
        mid = (s + e) // 2
        
        a, b = A * mid / 100, B * mid / 100
        ok = 0 if a > C or b > D else 1
        
        if ok : 
            s = mid + 1
            answer = mid
        else : 
            e = mid-1
    print(f"{answer}%")