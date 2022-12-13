n = int(input())
a = list(map(int, input().split()))
y, z = map(int, input().split())
answer = []

for i in a : 
    if int(i) >= z : 
        answer.append(int(i))

print(f'{round((n * (y / 100)))} {len(answer)}')