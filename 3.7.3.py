# n1 = int(input())
n1 = 4
s = ''
for i in range(n1):
    s += (input() + ' ').lower()
s = s.split()
# n2 = int(input())
n2 = 3
s1 = ''
for i in range(n2):
    s1 += (input() + ' ').lower()
s1 = s1.split()

uncorrects = []
for i in s1:
    if i not in s and i not in uncorrects:
        uncorrects.append(i)
for i in uncorrects:
    print(i)
