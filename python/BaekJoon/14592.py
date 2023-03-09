N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
s = sorted(li, key=lambda x:(-x[0], x[1], x[2]))
print(li.index(s[0])+1)