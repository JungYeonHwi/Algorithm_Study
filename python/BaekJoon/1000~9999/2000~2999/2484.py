N = int(input())
List = []

for i in range(N) : 
    money = 0
    A, B, C, D = map(int, input().split())
    
    if (A == B and B == C and C == D) : money = 50000 + A * 5000
    
    elif (A == B and B == C) : money = 10000 + A * 1000
    elif (B == C and C == D) : money = 10000 + B * 1000
    elif (A == C and C == D) : money = 10000 + C * 1000
    elif (A == B and B == D) : money = 10000 + D * 1000
    
    elif (A == B and C == D) : money = 2000 + A * 500 + C * 500
    elif (A == D and B == C) : money = 2000 + A * 500 + C * 500
    elif (A == C and B == D) : money = 2000 + A * 500 + B * 500
    
    elif (A == B and B != C and B != D) : money = 1000 + A * 100
    elif (A == C and B != C and C != D) : money = 1000 + A * 100
    elif (A == D and D != C and C != D) : money = 1000 + A * 100
    elif (B == C and B != A and C != D) : money = 1000 + B * 100
    elif (B == D and B != A and C != D) : money = 1000 + B * 100
    elif (D == C and D != A and B != D) : money = 1000 + C * 100
    
    else : money = max(A, B, C, D) * 100
    
    List.append(money)
    
print(max(List))