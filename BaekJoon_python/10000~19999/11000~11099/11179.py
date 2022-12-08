n = int(input())
num = bin(n)[2:][::-1]

answer = int(num, 2)
print(answer)