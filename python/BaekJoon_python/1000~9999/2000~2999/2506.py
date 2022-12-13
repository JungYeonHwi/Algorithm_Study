n = int(input())
s = 0
result = 0
List = list(map(int, input().split()))

for i in range(n):
    if List[i] == 1:
        s += 1
        result += s
    else:
        s = 0

print(result)