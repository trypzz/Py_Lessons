a = int(input())
b = int(input())
summ = 0
count = 0
for i in range (a,b+1):
    if i%3 == 0:
        count = count + 1
        summ = summ + i
print (summ/count)
