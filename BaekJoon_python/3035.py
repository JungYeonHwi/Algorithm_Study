i = 0
new = []
res = ''
a, b, c, d = map(int, input().split())

for i in range(a) :
    article = input()
    for k in range(c) :
        for j in range(b) :
            res += article[j] * d
        new.append(res)
        res = ''
        
for i in new :
    print(i)