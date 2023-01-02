melon = int(input()) 
values = [input().split() for _ in range(6)]
directions = [int(v[0]) for v in values] 
lengths = [int(v[1]) for v in values] 
l, boxLen = [], [] 

for i in range(1, 5):
    if directions.count(i) == 1: 
        l.append(lengths[directions.index(i)]) 
        temp = directions.index(i) + 3
        if temp >= 6:
            temp -= 6 
        boxLen.append(lengths[temp]) 

area = l[0] * l[1] - boxLen[0] * boxLen[1]
print(melon * area)