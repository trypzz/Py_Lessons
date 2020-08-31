b = input()
avg = 0
if b != '':
    for a in b.split():
        if a == 'A':
            avg = avg + 1
    print("%.2f" % (avg / len(b.split())))
    # __round__(3)
