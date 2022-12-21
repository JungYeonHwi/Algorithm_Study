w = float(input())
h = float(input())

answer = w / (h * h)

if answer > 25 : print("Overweight")
elif 18.5 <= answer <= 25.0 : print("Normal weight")
else : print("Underweight")