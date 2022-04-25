n = int(input())

u = set()
for i in range(n):
    u.add(int(input()))

s = set()
for i in u:
    for j in u:
        s.add(i + j)

ans = {}
for i in u:
    for j in u:
        if (i - j) in s:
            ans[i] = (i, j, i - j)

keys = list(ans.keys())
keys.sort(reverse=True)
print(keys[0])