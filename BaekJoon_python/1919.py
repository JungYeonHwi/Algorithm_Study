x = input()
y = input()

result=0

for i in range(len(x)) :
    for j in range(len(y)) :
        if x[i]!=" " and x[i] == y[j] :
            z = x[i]
            x = x.replace(x[i], " ", 1)
            y = y.replace(y[j], " ", 1)
            break

for i in range(len(x)) :
    if x[i]!=' ' : result += 1

for i in range(len(y)) :
    if y[i]!=' ' : result += 1

print(result)