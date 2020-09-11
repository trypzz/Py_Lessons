s=[int(i) for i in input().split()]
s.sort()
m=[]
for i in range(len(s)):
    if i>0:
        if s[i]==s[i-1]:
            if s[i] not in m:
                m+=[s[i]]
for i in m:
    print(i, end=" ")