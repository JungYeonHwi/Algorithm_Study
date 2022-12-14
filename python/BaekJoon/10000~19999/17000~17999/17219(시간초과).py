n, m = map(int, input().split())

site = []
pw = []

for _ in range(n) : 
    a, b = map(str, input().split())
    site.append(a)
    pw.append(b)
    
for _ in range(m) : 
    s = input()
    idx = site.index(s)
    print(pw[idx])