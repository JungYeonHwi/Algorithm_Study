n = int(input())
s = input()

answer = 0

for i in s : 
    answer += ord(i) - 64

print(answer)