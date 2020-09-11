f = open('table','r')
klas = {'1':[0,0],'2':[0,0],'3':[0,0],'4':[0,0],'5':[0,0],'6':[0,0],'7':[0,0],'8':[0,0],'9':[0,0],'10':[0,0],'11':[0,0]}
for s in f.readlines():
    s = s.strip().split('\t')
    lst = klas[s[0]]
    lst[0] += int(s[2])
    lst[1] += 1

for i in klas:
    lst = klas[i]
    print(i,lst[0]/lst[1])