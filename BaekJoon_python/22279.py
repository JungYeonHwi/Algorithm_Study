s = 0

for _ in range(int(input())) : 
    a, b = map(float, input().split())
    s += (a * b)
    
print(f'{s:.3f}')