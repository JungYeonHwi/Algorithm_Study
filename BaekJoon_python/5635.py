List = []
T = int(input())

for _ in range(T):
    n, d, m, y = input().split()
    List.append([n, int(d), int(m), int(y)])
    
List.sort(key=lambda x:(x[3],x[2],x[1]))
print(List[-1][0])
print(List[0][0])