List = []
A, B = map(int, input().split())
S = B

for i in range(3) : 
    A, B = map(int, input().split())
    S = S + B - A
    List.append(S)
    
print(max(List))