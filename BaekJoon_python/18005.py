n = int(input())

answer = 0

if n % 2 : answer = 0
elif n // 2 % 2 == 0 : answer = 2
else : answer = 1
print(answer)