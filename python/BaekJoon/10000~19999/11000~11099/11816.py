X = input()

if (X[0] == '0' and X[1] == 'x') : 
    data = int(X[2:], 16)
    print(data)
    
elif (X[0] == '0') : 
    data = int(X[1:], 8)
    print(data)

else : print(int(X))