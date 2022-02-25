T = int(input())

for i in range(T) : 
    List = list(map(int, input().split()))
    sortedList = sorted(List, reverse=True)
    
    print(sortedList[2])