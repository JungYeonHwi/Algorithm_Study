from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()
arr = []
for i in range(0, len(s), n) :
    arr.append(list(s[i:i+n]))

for i in range(len(arr)) :
    if i % 2 != 0:
        data = list(reversed(arr[i]))
        arr[i] = data

answer = ''
for j in range(n):
    for i in range(len(arr)):
        answer += arr[i][j]
print(answer)