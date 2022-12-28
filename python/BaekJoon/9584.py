value = input()
answer = []

for _ in range(int(input())) :
    check = input()
    
    tmp = 1
    
    for i in range(len(value)) : 
        if value[i] == "*" : continue
        else : 
            if value[i] != check[i] : 
                tmp = 0
                break

    if tmp : answer.append(check)
    
print(len(answer))
for i in answer : 
    print(i)
