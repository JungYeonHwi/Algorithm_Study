N = int(input())
List = []

for i in range(N) : 
    money = 0
    A, B, C = map(int, input().split())
    
    if (A == B and B == C) : money = 10000 + A * 1000
    elif (A == B) : money = 1000 + A * 100
    elif (B == C) : money = 1000 + B * 100
    elif (A == C) : money = 1000 + C * 100
    else : money = max(A, B, C) * 100
    
    List.append(money)
    
print(max(List))