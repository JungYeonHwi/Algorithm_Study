n = float(input())
k = list(map(int, input().split())) 

k.sort(reverse = True)

result = 0
count = 1
for i in k:
    if count == 1:
        count += 1
        result += i
        continue
    else:
        result += (i/2)
print(result)