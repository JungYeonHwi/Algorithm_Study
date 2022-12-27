answer = 0

for _ in range(int(input())) : 
    a, b = map(int, input().split())
    front = a * b
    top = b - 1
    
    answer += front
    
print(answer)
    