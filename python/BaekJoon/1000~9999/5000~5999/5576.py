W = []
K = []

for i in range(10) : 
    n = int(input())
    W.append(n)
    
for i in range(10) : 
    n = int(input())
    K.append(n)
    
sortedW = sorted(W, reverse=True)
sortedK = sorted(K, reverse=True)

WS = 0
KS = 0

for i in sortedW[:3] : WS += i
for i in sortedK[:3] : KS += i
    
print(WS, KS)