# s = input().lower()
s = "a aa abC aa ac abc bcd a".lower()
s = s.split()
d = {}
count = 0
for i in s:
    d[i]=0
    for j in s:
        if i == j:
            d[i] += 1
for i in d:
    print(i,d[i])