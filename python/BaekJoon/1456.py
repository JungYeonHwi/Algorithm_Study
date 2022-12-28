import sys, math
input = sys.stdin.readline

m, n = map(int, sys.stdin.readline().split())

primeList = [True] * (int(n ** 0.5) + 1)
primeList[1] = False

for i in range(2, int(n ** 0.5) + 1) :
    if primeList[i]:
        if i * i > int(n ** 0.5):
            break
        for j in range(i**2, int(n ** 0.5) + 1, i):
            primeList[j] = False

count = 0
for i in range(1, len(primeList)) :
    if primeList[i] :
        res = i * i
        while 1 :
            if res < m :
                res *= i
                continue
            if res > n:
                break
            res *= i
            count += 1

print(count)