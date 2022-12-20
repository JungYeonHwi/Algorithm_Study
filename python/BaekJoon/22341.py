n, c = map(int, input().split())
a = n
b = n
for _ in range(c) :
    y, x = map(int, input().split())
    
    if x * a <= y * b : a = y
    else : b = x

print(a * b)