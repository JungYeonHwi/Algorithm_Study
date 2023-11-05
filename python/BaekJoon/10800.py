import sys
input = sys.stdin.readline

N = int(input())
arr = []
result = [0] * (N + 1)
color = [0] * (N + 1)
weight = [0] * 2001
for i in range(N):
    e1, e2 = map(int, input().split())
    arr.append((e2,e1,i))
arr.sort() # 정렬은 무게, 색깔순으로
prefix_sum = [0] * (N + 1)

for i in range(0, N):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i][0]
    
    if i>0 and arr[i][1]==arr[i-1][1] and arr[i][0]==arr[i-1][0]:
        # 색과 무게가 동시에 같을 경우 이전 값으로
        result[arr[i][2]]=result[arr[i-1][2]]
    else:
    	# 같은 색 빼기, 같은 무게 빼기
        result[arr[i][2]]=prefix_sum[i-1]-color[arr[i][1]]-weight[arr[i][0]]
    
    color[arr[i][1]]+=arr[i][0]
    weight[arr[i][0]]+=arr[i][0]

for i in range(0, N):
    print(result[i])
