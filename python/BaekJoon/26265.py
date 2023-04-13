import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(((sys.stdin.readline().split())))

arr.sort()
arr2 = {}
for i in arr:
    if i[0] in arr2.keys():
        arr2[i[0]].append(i[1])
    else:
        arr2[i[0]] = [i[1]]
for i in arr2:
    arr2[i].sort(reverse = True)

for i in arr2:
    for j in arr2[i]:
        print(i, j)