import sys

t = int(sys.stdin.readline())

for _ in range(t) : 
    sound = list(map(str, sys.stdin.readline().split()))
    
    while 1 : 
        animal = list(map(str, sys.stdin.readline().split()))
        if animal[0] == "what" :
            print(" ".join(sound))
            break

        while animal[2] in sound : sound.remove(animal[2])