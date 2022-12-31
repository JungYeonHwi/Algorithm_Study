n, k = map(int, input().split())
circle = ['?'] * n

for i in range(k):
    spin = input().split()
    
    s = int(spin[0]) % n
    idx = str(spin[1])
    circle = circle[-s:] + circle[:-s]	

    if circle[0] == '?':
        if idx in circle:
            print('!')
            break
        circle[0] = idx
    elif circle[0] == idx:
        continue
    else:
        print('!')
        break
else:
    print("".join(circle))