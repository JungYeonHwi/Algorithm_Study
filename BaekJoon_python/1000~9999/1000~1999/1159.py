li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []

for c in s:
    if li.count(c) >= 5 :
        res.append(c)
if len(res) > 0 : print(''.join(sorted(res)))
else : print("PREDAJA")