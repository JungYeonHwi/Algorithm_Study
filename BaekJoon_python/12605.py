n = int(input())

for _ in range(n) : 
    List = list(map(str, input().split()))
    reversedList = List[::-1]
    s = " ".join(reversedList)
    print("Case #%d: %s" %(_+1, s))