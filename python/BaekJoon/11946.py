n, m, q = map(int,input().split())
dic = {}
for i in range(1, n+1):
	for j in range(1, m+1):
		dic[(i, j)] = [0, -1]
for _ in range(q):
	log = input().split()
	if log[3] != 'AC':
		dic[(int(log[1]), int(log[2]))][0] += 1
	else:
		if dic[(int(log[1]), int(log[2]))][1] < 0:
			dic[(int(log[1]), int(log[2]))][1] = dic[(int(log[1]), int(log[2]))][0] * 20 + int(log[0])
dab = [[i,0,0] for i in range(1, n+1)]
for i in range(1, n+1):
	for j in range(1, m+1):
		if dic[(i,j)][1] >= 0:
			dab[i-1][1] += 1
			dab[i-1][2] += dic[(i,j)][1]
dab.sort(key = lambda x: (-x[1], x[2], x[0]))
for i in dab:
	print(*i)