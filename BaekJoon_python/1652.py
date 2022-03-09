n = int(input())
s = []
cnt_w = 0
cnt_h = 0
position_w = 0
position_h = 0

for i in range(n) :
    s.append(input())
for i in s :
    for j in i :
        if j == '.' :
            cnt_w += 1
        else :
            if cnt_w > 1 :
                position_w += 1
            cnt_w = 0
    if cnt_w > 1 :
        position_w += 1
        
    cnt_w = 0
    
for i in range(n) :
    for j in range(n) :
        if s[j][i] == '.' :
            cnt_h += 1
        else :
            if cnt_h > 1 :
                position_h += 1
            cnt_h = 0
    if cnt_h > 1 :
        position_h += 1
        
    cnt_h = 0
    
print(position_w, position_h)