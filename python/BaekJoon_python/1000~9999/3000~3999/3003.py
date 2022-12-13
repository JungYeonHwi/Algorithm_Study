cp = [1, 1, 2, 2, 2, 8]
List = list(map(int, input().split()))

for i in range(6):
    print(cp[i]-List[i], end=' ')