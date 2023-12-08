def check(s):
    global result
    if len(s) == len(S): # 길이가 같고
        if s == S: # 모양 같으면
            result = 1 
            return # 끝
        return 
    if s[-1] == 'A': # 끝자리가 A면
        s.pop() # 빼보고
        check(s) # 다시 탐색
        s.append('A') # 아니었다면 다시 복구
    if s[0] == 'B': # 앞자리가 B면 
        s.reverse() # 뒤집어서
        s.pop() # 꺼내고
        check(s) # 다시 탐색
        s.append('B')
        s.reverse()
    
import sys
S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
result = 0
check(T)
print(result)
