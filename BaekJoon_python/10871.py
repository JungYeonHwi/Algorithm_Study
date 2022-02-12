N, X = map(int, input().split())
List = list(map(int, input().split()))

for i in range(len(List)) : 
    if (X > List[i]) : print(List[i], end=' ')