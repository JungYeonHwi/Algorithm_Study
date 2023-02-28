s = input()[::-1]
answer = ""
arr = []

for i in range(0, len(s), 3) : 
    arr.append(s[i:i+3])

arr.reverse()

for i in arr : 
    answer += i[::-1] + ","
    
answer = answer[:-1:]

print(answer)