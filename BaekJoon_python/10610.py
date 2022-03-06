n = list(input())
n.sort(reverse=True)
s = 0

for i in n : s += int(i)
if s % 3 != 0 or "0" not in n : print(-1)
else : print(''.join(n))