A, B = map(int, input().split())
answer = ""

for i in range(1, 25) : 
    if A >= 5 : 
        answer = "yj"
        break
    if B >= 5 : 
        answer = "yt"
        break

    if i % 2 != 0 : 
        A = A
        B = B + A
    else : 
        B = B
        A = A + B
        
print(answer)