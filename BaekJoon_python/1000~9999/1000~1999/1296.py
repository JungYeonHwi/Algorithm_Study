ms = input()
n = int(input())
li = sorted([input() for i in range(n)])
maxP = maxI = 0

for i in range(n):
    L = ms.count("L") + li[i].count("L")
    O = ms.count("O") + li[i].count("O")
    V = ms.count("V") + li[i].count("V")
    E = ms.count("E") + li[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    
    if maxP < p:
        maxP = p
        maxI = i
print(li[maxI])