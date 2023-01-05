from itertools import permutations

a, b = input().split()
b = int(b)
c = -1

arr = []
for item in permutations(a):
    arr.append(''.join(item))

for i in arr:
    if i[0] == '0': 
        continue
    i = int(i)
    if i < b :
        c = max(c, i)

print(c)