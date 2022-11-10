a, b = map(int, input().split())
n = list(map(int, input().split()))
n.sort()

for i in range(a) :
    if b >= int(n[i]):
        b += 1
print(b)