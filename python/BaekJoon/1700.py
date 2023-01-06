N, K = map(int, input().split())
scheduling = list(map(int, input().split()))

adaptor = [0] * N
count = 0
idx = 0
tmp = 0
tmpValue = 0

for i in scheduling:
    if i in adaptor:
        pass
    elif 0 in adaptor:
        adaptor[adaptor.index(0)] = i
    else:
        for j in adaptor:
            if j not in scheduling[idx:]:
                tmp = j
                break
            elif scheduling[idx:].index(j) > tmpValue: 
                tmp = j
                tmpValue = scheduling[idx:].index(j)
        adaptor[adaptor.index(tmp)] = i
        tmp = tmpValue = 0
        count += 1
    idx += 1

print(count)