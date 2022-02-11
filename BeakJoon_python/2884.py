H, M = map(int, input().split())

if (M >= 45) :
	h = H;
	m = M - 45;

else : 
    if (H == 0) :
        h = 23
	    m = 60 + M - 45
    else : 
        h = H - 1
		m = 60 + M - 45

print(h m)