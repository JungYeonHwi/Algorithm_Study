N = int(input())
List = [float(input()) for _ in range(N)]

for i in range(1, N):
    List[i] = max(List[i], List[i]*List[i-1])
    
print("%.3f" % (max(List)))