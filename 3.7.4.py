# n = 4
x = 0
y = 0
n = int(input())
for i in range(n):
    na = input().strip().split()
    if na[0] == 'север':
        y += int(na[1])
    if na[0] == 'запад':
        x -= int(na[1])
    if na[0] == 'юг':
        y -= int(na[1])
    if na[0] == 'восток':
        x += int(na[1])

print(x,y)