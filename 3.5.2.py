import sys
count = 0
for i in sys.argv:
    count += 1
    if count != 1:
        print(i, end=' ')