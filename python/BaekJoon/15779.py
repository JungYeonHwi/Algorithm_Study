n = int(input())
arr = list(map(int,input().split()))
ml = 2
cnt = 2
for i in range(n-2) :
	if arr[i] <= arr[i+1] and arr[i+1] <= arr[i+2] :
		cnt = 2

	elif arr[i] >= arr[i+1] and arr[i+1] >= arr[i+2] :
		cnt = 2

	else : 
		cnt += 1
	ml = max(ml,cnt)
print(ml)