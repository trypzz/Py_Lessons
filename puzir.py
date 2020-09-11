s = [5,2,3,76,1,32,6,2,7]
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] < s[j]:
            tmp=s[i]
            s[i] = s[j]
            s[j] = tmp
print(s)