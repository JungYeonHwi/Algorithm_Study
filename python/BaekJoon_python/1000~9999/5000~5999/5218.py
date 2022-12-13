t = int(input())
alp = [chr(i) for i in range(65, 91)]

for i in range(t) :
    res = []
    x, y = input().split()
    
    for j in range(len(x)) :
        if alp.index(y[j]) >= alp.index(x[j]) :
            res.append(alp.index(y[j]) - alp.index(x[j]))
        elif alp.index(y[j]) < alp.index(x[j]) :
            res.append((alp.index(y[j]) + 26) - alp.index(x[j]))
    
    print('Distances:', *res)