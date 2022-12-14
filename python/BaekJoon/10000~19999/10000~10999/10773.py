K = int(input())
List = []

for i in range(K) : 
    n = int(input())
    if n == 0 : List.pop()
    else : List.append(n)

print(sum(List))