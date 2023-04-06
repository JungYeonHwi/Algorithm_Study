t, p = map(int, input().strip().split())
if p >= 20 : print(t / (100 - p) * (p + 20))
else : print(t / (80 + (20 - p) * 2) * p * 2)