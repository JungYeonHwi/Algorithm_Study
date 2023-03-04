s = input()
arr = [0 for i in range(8)]
for i in s:
    if i in '1QAZ':
        arr[0] += 1
    elif i in '2WSX':
        arr[1] += 1
    elif i in '3EDC':
        arr[2] += 1
    elif i in '45RTFGVB':
        arr[3] += 1
    elif i in '67YUHJNM':
        arr[4] += 1
    elif i in '8IK,':
        arr[5] += 1
    elif i in '9OL.':
        arr[6] += 1
    else:
        arr[7] += 1
for i in arr:
    print(i)