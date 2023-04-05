for _ in range(int(input())):
    text = input()
    t = text.split()
    
    t = [text[::-1] for text in t][::-1]
    answer = " ".join(t)
    print(answer)