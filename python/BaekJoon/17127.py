def recur(remainder, length):
    global answer
 
    if length == 0 :
        if remainder == 0 :
            v = 0
            lm = 0
            for i in tmp :
                lm += mul(a[v:v+i])
                v += i
            answer = max(answer, lm)
        return
 
    for i in range(1,remainder+1):
        tmp.append(i)
        recur(remainder-i, length-1)
        tmp.pop()
 
def mul(arr) :
    a = 1
    for i in range(len(arr)):
        a *= arr[i]
    return a
 
n = int(input())
a = list(map(int, input().split()))
tmp = []
answer = 0
recur(n, 4)
print(answer)
