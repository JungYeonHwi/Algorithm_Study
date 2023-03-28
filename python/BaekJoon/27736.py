n = int(input())

ckstjd = 0
qkseo = 0
rlrnjs = 0

arr = list(map(int, input().split()))

for i in arr : 
    if i == 1 : ckstjd += 1
    if i == -1 : qkseo += 1
    if i == 0 : rlrnjs += 1
    
answer = ""
    
if rlrnjs >= n / 2 : answer = "INVALID"
elif ckstjd > qkseo : answer = "APPROVED"
else : answer = "REJECTED"

print(answer)