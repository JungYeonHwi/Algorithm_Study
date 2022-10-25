cards = [i for i in range(1, 21)]

for _ in range(10) : 
    a, b = map(int, input().split())
    
    tmp = list(cards[a-1:b])
    tmp.reverse()
    cards[a-1:b] = tmp
        
for i in cards : 
    print(i, end=" ")