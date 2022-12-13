import sys
input = sys.stdin.readline

while 1 :
    s = input().rstrip()
    if s == "*" : break
    else : 
        state = 1
        for i in range(1, len(s)) :
            arr = []
            for j in range(len(s)-i) : arr.append(s[j] + s[j+i])
            for k in range(len(arr)-1) :
                if arr[k] in arr[k+1:] : state = 0
        if state : print("{0} is surprising.".format(s))
        else : print("{0} is NOT surprising.".format(s))