s = input().split()
a = input()
ctrl = 0
for i in range(len(s)):
    if s[i] == a:
        print(s.index(a,i), end=" ")
        ctrl = 1
if ctrl == 0:
    print("Отсутствует")