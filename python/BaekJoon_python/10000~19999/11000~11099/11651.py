N = int(input())

List = []

for i in range(N) : 
    X, Y = map(int, input().split())
    List.append([Y, X])
    
sortedList = sorted(List)

for Y, X in sortedList :
    print(X, Y)