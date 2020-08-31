a = int(input())
b = int(input())
if a < b:
    d = b
else:
    d = a

while d%a != 0 or d%b != 0:
    d = d+1
print(d)