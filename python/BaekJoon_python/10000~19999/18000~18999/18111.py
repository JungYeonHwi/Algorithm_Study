import sys
from collections import Counter

n, m, inven = map(int, sys.stdin.readline().split())
ground = []
for _ in range(n): ground += map(int, sys.stdin.readline().split())
height, time = 0, 1000000000000000

minH = min(ground)
maxH = max(ground)
s = sum(ground)
ground = dict(Counter(ground))

for i in range(minH, maxH + 1) :
    if s + inven >= i * n * m :
        t = 0
        for key in ground :
            if key > i : t += (key - i) * ground[key] * 2
            elif key < i : t += (i - key) * ground[key]
        if t <= time :
            time = t
            height = i

print(time, height)