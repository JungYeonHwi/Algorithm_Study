n = int(input())

List = list(map(int, input().split()))

s = set(List)

sortedList = sorted(list(s))
dic = {sortedList[i] : i for i in range(len(sortedList))}

for i in List :
    print(dic[i], end = ' ')