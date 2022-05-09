n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
s = 0

for i in range(0, b - 2) :
    for j in range(i + 1, b - 1) :
        for k in range(j + 1, b) :
                print(a[i], a[j], a[k])
                if a[i] + a[j] + a[k] > m : continue
                else : s = max(s, a[i] + a[j] + a[k])
print(s)