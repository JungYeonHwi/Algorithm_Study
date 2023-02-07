from sys import stdin

N, K = map(int, stdin.readline().split(" "))

fk = K % 10

f2k = (2 * K) % 10

f = []

for x in range(1, N+1) : 
    fx = x % 10
    
    if fx != fk and fx != f2k : 
        f.append(str(x))
        
        
print(len(f))
print(" ".join(f))        