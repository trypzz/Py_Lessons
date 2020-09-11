s = input().lower()
count = 0
for i in s:
    if i == 'c' or i == "g":
        count = count + 1
print(count / len(s) * 100)