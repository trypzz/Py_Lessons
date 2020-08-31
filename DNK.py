s = input()
count = 1
result_s = ""
for i in range(0,len(s)):
    if i == len(s)-1:
        result_s = result_s + s[i] + str(count)
        break
    else:
        if s[i] == s[i+1]:
            count = count + 1
        else:
            result_s = result_s + s[i] + str(count)
            count = 1

print(result_s)