s = input().split()
if len(s) == 1:
    print(s[0])
else:
    for i in range(0, len(s)):
        if i == 0:
            print(int(s[i - 1]) + int(s[i + 1]), end=" ")
        else:
            if i == len(s) - 1:
                print(int(s[i - 1]) + int(s[0]), end=" ")
            else:
                print(int(s[i - 1]) + int(s[i + 1]), end=" ")
