List = list(map(str, input()))
height = 10

first = List[0]

for i in List[1:] : 
    if (first != i) : height += 10
    elif (first == i) : height += 5

    first = i

print(height)