# s = "abc a bCd bC AbC BC BCD bcd ABC".lower()
s = open("source").read()
most = s.lower()
s = s.lower().split()
print(s)
d = {}
for i in s:
    d[i]=0
    for j in s:
        if i == j:
            d[i] += 1
most_key = 0
for i in d:
    if d[i] > most_key:
        most_key = d[i]
        most = i
print(most,d[most])