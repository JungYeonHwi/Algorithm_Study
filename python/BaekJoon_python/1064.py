ax, ay, bx, by, cx, cy = map(int, input().split())

if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)) :
    print(-1.0)
    exit(0)

ab = ((ax-bx)**2 + (ay-by)**2)**0.5
ac = ((ax-cx)**2 + (ay-cy)**2)**0.5
bc = ((bx-cx)**2 + (by-cy)**2)**0.5

length = [ab+ac, ab+bc, ac+bc]
result = max(length) - min(length)
print(2*result)