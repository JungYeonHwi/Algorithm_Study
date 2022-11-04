arr = []

while 1 : 
    num = float(input())
    if num == 999 : break
    else : 
        arr.append(num)
        
for i in range(0, len(arr) - 1) : 
    num1 = arr[i]
    num2 = arr[i+1]
    print("%.2f" % (num2 - num1))