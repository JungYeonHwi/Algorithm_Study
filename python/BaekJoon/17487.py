S = input() 
left = 'qwertyasdfgzxcvb' 
right = 'uiophjklnm' 
cl, cr, co = 0, 0, 0 

for i in S: 
    if i.isupper(): 
        co += 1 
         
for i in S.lower(): 
    if i in right: 
        cr += 1 
    elif i in left: 
        cl += 1 
    else: 
        co += 1 

while co != 0: 
    if cl <= cr: 
        cl += 1 
    else: 
        cr += 1 
    co -= 1 
     
print(cl, cr)