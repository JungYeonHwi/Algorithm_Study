N = int(input())

List = []

for i in range(N) : 
    lst = list(map(int, input().split()))
    List.append(lst)
    
sortedList = sorted(List)

for i in range(N) :
    print(sortedList[i][0], sortedList[i][1])