R, C = map(int, input().split())
arr = []

for _ in range(R) : 
    arr.append(input())

zero = 0
one = 0
two = 0
three = 0
four = 0

for r in range(R) : 
    for c in range(C) : 
        if r+1 == R or c+1 == C : break
        w = arr[r][c]
        x = arr[r][c+1]
        y = arr[r+1][c]
        z = arr[r+1][c+1]
        
        tmp = w + x + y + z
        
        if "#" in tmp : continue
        else : 
            car = tmp.count("X")
            if car == 0 : zero += 1
            elif car == 1 : one += 1
            elif car == 2 : two += 1
            elif car == 3 : three += 1
            elif car == 4 : four += 1
        
print(zero)
print(one)
print(two)
print(three)
print(four)