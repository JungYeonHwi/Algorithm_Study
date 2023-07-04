N = int(input())
candy = list(map(int, input().split()))
result = 0
oc = []

for i in candy:
    if i % 2 == 1:	
        oc.append(i)
    else:
        result += i

if len(oc) % 2 == 1:
    oc.sort(reverse=True)
    del oc[-1]
    result += sum(oc)
else:
    result += sum(oc)

print(result)