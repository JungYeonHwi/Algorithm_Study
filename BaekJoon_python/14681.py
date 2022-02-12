x = int(input())
y = int(input())

if (x > 0 and y > 0) : pos = 1
elif (x < 0 and y > 0) : pos = 2
elif (x < 0 and y < 0) : pos = 3
else : pos = 4

print(pos)