import sys
import itertools

n = int(sys.stdin.readline())

wc = dict(zip(sys.stdin.readline().split(), [i for i in range(n)]))

wa = sys.stdin.readline().split()

pick = list(itertools.combinations(wa, 2))
point = 0  

for p in pick:
    if wc.get(p[0]) < wc.get(p[1]):
        point += 1

print("%d/%d" % (point, n*(n-1)/2))