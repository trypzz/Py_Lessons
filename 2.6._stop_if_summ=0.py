ar = ['0']
summ = 1
while summ != 0:
    ar.append(input())
    summ = 0
    for i in range(len(ar)):
        summ += int(ar[i])