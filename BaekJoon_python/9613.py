import math

n = int(input())

for _ in range(n) : 
    value = list(map(int, input().split()))
    List = value[1:]
    answer = []

    for i in range(0, len(List) - 1) : 
        for j in range(i+1, len(List)) : 
            answer.append(math.gcd(List[i], List[j]))
        
    print(sum(answer))