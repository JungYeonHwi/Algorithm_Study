N = int(input())

List = []

for num in range(N) : 
    test = list(input())
    value = 0
    answer = 0
    for i in range(len(test)) : 
        if(test[i] == "O") : 
            value = value + 1
            answer = answer + value
        else : 
            value = 0
    print(answer)