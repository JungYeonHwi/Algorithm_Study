A, B, G = 0, 0, 0
N = int(input())
List = list(map(str, input()))

for i in range(N) : 
    if i % 3 == 0 : 
        if List[i] == 'A' : A += 1
    elif i % 3 == 1 : 
        if List[i] == 'B' : A += 1
    else : 
        if List[i] == 'C' : A += 1
        
    if i % 4 == 0 or i % 4 == 2 : 
        if List[i] == 'B' : B += 1
    elif i % 4 == 1 : 
        if List[i] == 'A' : B += 1
    else : 
        if List[i] == 'C' : B += 1
        
    if i % 6 == 0 or i % 6 == 1 : 
        if List[i] == 'C' : G += 1
    elif i % 6 == 2 or i % 6 == 3 : 
        if List[i] == 'A' : G += 1
    else : 
        if List[i] == 'B' : G += 1
        
m = max(A, B, G)
print(m)

if m == A : print('Adrian')
if m == B : print('Bruno')
if m == G : print('Goran')