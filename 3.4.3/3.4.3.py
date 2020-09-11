avg_o = {'matematika': 0, 'fizika': 0, 'russkiy': 0}
count = 0
avg_ind = 0
w = open('result','a')
students = 0
for i in open('source').readlines():
    avg_ind = 0
    students += 1
    for j in i.strip().split(';'):
        if j.isdigit():
            avg_ind += int(j)
            count += 1
            if count == 1:
                avg_o['matematika'] += int(j)
            if count == 2:
                avg_o['fizika'] += int(j)
            if count == 3:
                avg_o['russkiy'] += int(j)
    count = 0
    w.writelines(str(avg_ind / 3) + '\n')
w.close()
for i in avg_o.values():
    open('result','a').writelines(str(i/students) + ' ')