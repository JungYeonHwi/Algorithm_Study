from sys import stdin
n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().split()))
result1 = 0
result2 = 0
p = 0
for i in a:
    if i%2==1:
        p+=1
    else:
        result1+=p
a.reverse()
p = 0
for i in a:
    if i%2==1:
        p+=1
    else:
        result2+=p
print(min(result1, result2))
