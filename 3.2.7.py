n = int(input())
s = {}
for i in range(n):
    x = int(input())
    if x not in s:
        s[x] = f(x)
        print (s[x])
    else:
        print (s[x])