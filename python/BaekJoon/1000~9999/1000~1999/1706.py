import sys

R, C = map(int, sys.stdin.readline().split())

arr = list()
for i in range(R) :
    arr.append(sys.stdin.readline().rstrip())

new = list(map(list, zip(*arr)))

answer = []
for i in range(R) :
    save = arr[i].split("#")
    for j in save :
        if len(j) > 1 :
            answer.append(j)

for i in range(C) :
    save = "".join(new[i]).split("#")
    for j in save :
        if len(j) > 1 :
            answer.append(j)

answer.sort()
print(answer[0])