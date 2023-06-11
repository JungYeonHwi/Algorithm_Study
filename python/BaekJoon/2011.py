from sys import stdin,setrecursionlimit
input = stdin.readline
code = input().strip()
if code[0] == "0" or not code[0].isdecimal(): 
    print("0")
    exit()
mod = 1000000
cache = [1, 1] # 0번 인덱스와 1번 인덱스 연산을 위해 1 ,1 로 초기화해준다. 
for i in range(1, len(code)):
    cnt = 0
    if int(code[i]) > 0 and code[i].isdecimal():
        cnt += cache[-1] # 지금 관찰하는 i인덱스의 바로 앞 값 i-1 인덱스까지 만들 수 있는 개수를 더해준다.
    if 10<= int(code[i-1:i+1])<27:
        cnt += cache[-2] # i-2번째까지의 암호 개수에 i-1,i 인덱스의 숫자를 2자리 숫자로 넣는 개념
    cache.append(cnt%mod)
print(cache[-1])
