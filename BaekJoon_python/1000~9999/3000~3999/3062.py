t = int(input())

for _ in range(t) : 
    num = list(map(str, input()))
    reverseNum = list(num)
    reverseNum.reverse()
    result = 0
    
    a = "".join(num)
    A = int(a)
    b = "".join(reverseNum)
    B = int(b)
    
    result = str(A + B)
    
    if result == result[::-1] : print("YES")
    else : print("NO")