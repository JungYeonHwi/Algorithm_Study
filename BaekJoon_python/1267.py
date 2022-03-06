n = int(input())
List = list(map(int, input().split()))
y = 0
m = 0

for i in List : 
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y > m : print("M", m)
elif y < m : print("Y", y)
else : print("Y M", y)