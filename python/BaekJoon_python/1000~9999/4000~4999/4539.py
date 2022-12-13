a = int(input())
arr = []

for i in range(0,a):
    arr.append(input())

result = []
for i in range(0, len(arr)) :
    length = len(list(str(arr[i])))
    k = arr[i]
    for j in range(1, length):
        if str(k)[length-j:length-j+1] == '5' : 
            k = str(int(k) + 10**(j-1))
        k = round(int(k),-j)
    result.append(k)

for i in range(0, len(result)) : 
    print(result[i])
