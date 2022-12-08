N = int(input())
pos = list(map(int, input().split()))

answer = []

rate = 1

for potion in pos:
    rate *= (1 - potion / 100) 
    
    calculated_rate = (1 - rate) * 100
    
    answer.append(round(calculated_rate, 6))
    
for i in answer : 
    print(i)
    