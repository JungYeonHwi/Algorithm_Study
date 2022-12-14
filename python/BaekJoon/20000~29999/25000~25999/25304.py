X = int(input())

n = int(input())

for _ in range(n) : 
    
    a, b = map(int, input().split())
    cal = a * b
    
    X -= cal
    
if X == 0 : print("Yes")
else : print("No")