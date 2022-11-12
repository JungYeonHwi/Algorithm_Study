from sys import stdin

n, m = map(int, stdin.readline().split())
a = set(map(int, stdin.readline().split()))
b = set(map(int, stdin.readline().split()))

answer = a - b

if answer :
    print(len(answer))
    print(*sorted(list(answer)))
else : print(0)