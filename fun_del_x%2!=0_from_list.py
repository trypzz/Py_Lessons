def modify_list(l):
    for i in range(len(l),-1,-1):
        try:
            if (l[i]%2 != 0):
                l.pop(i)
        except IndexError as e: pass
    for i in range(len(l)):
        l[i] = int(l[i]/2)

lst = [-1,0,-5,-6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
