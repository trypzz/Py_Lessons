import math
fig = input()
if fig == "треугольник":
    a=int(input())
    b=int(input())
    c=int(input())
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
if fig == "прямоугольник":
    a = int(input())
    b = int(input())
    s = a*b
if fig == "круг":
    r = int(input())
    s = 3.14*r**2
print(float(s))