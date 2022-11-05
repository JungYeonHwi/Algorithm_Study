X, Y = map(int, input().split())
arr = [X / Y]
for _ in range(int(input())) :
    X, Y = map(int, input().split())
    arr.append(X / Y)
    
print("%.2f" % (min(arr) * 1000))