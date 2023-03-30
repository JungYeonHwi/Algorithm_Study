from sys import stdin

isbn = stdin.readline().rstrip()
l = len(isbn)

s = 0

idx = None

for i in range(l) : 
    if isbn[i] == "*" : 
        idx = i
        continue
    elif i % 2 == 0 : 
        s += int(isbn[i])
    elif i % 2 == 1 : 
        s += int(isbn[i]) * 3
        
for n in range(10) : 
    if s % 2 == 0 : 
        if (s + n) % 10 == 0 : 
            print(n)
            break
        else : 
            if (s + n * 3) % 10 == 0 : 
                print(n)
                break
    