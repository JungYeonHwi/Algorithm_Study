from sys import stdin

s = stdin.readline().rstrip()

for i in s : 
    c = ord(i)
    pos = sum(map(int, list(str(c))))
    
    print(i * pos)