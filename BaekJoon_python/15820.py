s1, s2 = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(s1)]
arr2 = [list(map(int, input().split())) for _ in range(s2)]

for i in range(s1) :
    if arr1[i][0] != arr1[i][1] :
        print("Wrong Answer")
        exit()
for i in range(s2):
    if arr2[i][0] != arr2[i][1 ]:
        print("Why Wrong!!!")
        exit()
print("Accepted")