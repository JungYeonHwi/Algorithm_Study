import sys

moves = int(sys.stdin.readline()) 
sample = list(map(int, sys.stdin.readline().split())) 
numShapes = int(sys.stdin.readline())
shapes = [] 
for _ in range(numShapes):
    shapes.append(list(map(int, sys.stdin.readline().split())))

reverse = {1:3, 2:4, 3:1, 4:2}
sames = []
for shape in shapes:
    reverse_shape = list(map(lambda x: reverse[x], shape))[::-1] 
    
    if shape == sample or reverse_shape == sample:
        sames.append(shape)
        continue
    
    for i in range(1, moves):
        tmp = shape[i:] + shape[:i]
        reverseTmp = reverse_shape[i:] + reverse_shape[:i]
        if tmp == sample or reverseTmp == sample:
            sames.append(shape)
            break

print(len(sames))
for s in sames:
    print(' '.join(list(map(str, s))))