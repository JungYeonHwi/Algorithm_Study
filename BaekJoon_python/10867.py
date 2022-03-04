N = int(input())

List = list(map(int, input().split()))
s = set(List)

l = list(s)

for i in sorted(l) : 
    print(i, end = ' ')