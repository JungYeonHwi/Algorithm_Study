n = int(input())
s = input()

if s[n-1] == "G" : answer = s[0:n-1]
else : answer = s + "G"

print(answer)