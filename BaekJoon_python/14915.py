number, n = map(int, input().split())

answer = ""
temp = list("0123456789ABCDEF")

if number == 0 : answer = "0"
else :
    while number :
        answer += temp[number % n]
        number //= n
        
print(answer[::-1])