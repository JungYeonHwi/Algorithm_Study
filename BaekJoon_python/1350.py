n = int(input())
s = list(map(int, input().split()))
a = int(input())
sm = 0

for i in s :
    if i % a == 0 :
        sm += i // a
    else :
        sm += i // a + 1
print(sm * a)