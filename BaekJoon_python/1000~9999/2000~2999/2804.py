a, b = map(str, input().split())
r = 0
c = 0

for i in range(len(a)) :
    index = b.find(a[i])
    if 0 <= index :
        r = index
        c = i
        break
    
for i in range(len(b)) :
    for j in range(len(a)) :
        if i == r :
            print(a, end='')
            break
        elif j == c :
            print(b[i], end='')
        else :
            print('.', end='')
    print()