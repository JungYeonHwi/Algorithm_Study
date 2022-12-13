num = int(input())
result = []

for i in range(1, num+1) :
    if num % i == 0 :
        result.append(i)

answer = sum(result) * 5 - 24

print(answer)