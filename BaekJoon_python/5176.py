K = int(input())

for i in range(K) : 
    wants = []
    count = 0
    people, seat = map(int, input().split())
    
    for i in range(people):
        wants.append(int(input()))
        
    if seat == 1 :
        print(people - 1)
        
    else :
        count = 0
        for i in range(1, seat+1):
            if wants.count(i) >= 2:
                count += wants.count(i) - 1
        print(count)