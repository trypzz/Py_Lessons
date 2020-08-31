a = float(input())
b = float(input())
e = input()

if e == "+":
    print(a + b)
if e == "-":
    print(a - b)
if e == "/":
    if b == 0.0:
        print("Деление на 0!")
    else:
        print(a / b)
if e == "*":
    print(a * b)
if e =="mod":
    if b == 0.0:
        print("Деление на 0!")
    else:
        print(a%b)
if e == "pow":
    print(a**b)
if e == "div":
    if b == 0.0:
        print("Деление на 0!")
    else:
        print(int(a)//int(b))