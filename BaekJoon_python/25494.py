n = int(input())

for _ in range(n) : 
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
