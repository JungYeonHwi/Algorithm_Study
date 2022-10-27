y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
manOld = 0
if m1 < m2: manOld = y2 - y1
elif m1 == m2 : 
    if d1 <= d2 : manOld = y2-y1
    else : manOld = y2-y1-1
else : manOld = y2-y1-1

countOld = y2-y1+1
yearOld = y2-y1

print(manOld)
print(countOld)
print(yearOld)