x, y, p1, p2 = map(int,input().split())

X = [p1]
Y = [p2]
spot = -1

for i in range(1000) : 
    X.append(X[i] + x)
    Y.append(Y[i] + y)
    
    if X[i] + x in Y or Y[i] + y in X : 
        spot = min(X[i] + x, Y[i] + y)
        break

print(spot)