import sys
input = sys.stdin.readline

n = int(input())
kk, jj, ii = 0, 0, 0
min = 1000001


for i in range(n) : 
    for j in range(n) : 
        if i * j > n : break
        
        for k in range(n) : 
            if i * j * k > n : break
            elif i * j * k < n : continue
            else : 
                size = i * j * 2 + i * k * 2 + j * k * 2
                if size < min : 
                    min = size
                    kk = k
                    jj = j
                    ii = i
                    
                break
            
print(kk, jj, ii)