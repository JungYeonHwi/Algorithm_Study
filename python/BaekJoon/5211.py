line = input().strip().split("|")

adeMinor = ['A', 'D', 'E']
cfgMajor = ['C', 'F', 'G']

adeMinorCnt = 0
cfgMajorCnt = 0

for i in line:
    if i[0] in adeMinor:
        adeMinorCnt += 1
    if i[0] in cfgMajor:
        cfgMajorCnt += 1
        
if adeMinorCnt == cfgMajorCnt :
    if line[-1][-1] in cfgMajor : 
        cfgMajorCnt += 1
    if line[-1][-1] in adeMinor :
        adeMinorCnt += 1

if adeMinorCnt < cfgMajorCnt : print("C-major")
else : print("A-minor")